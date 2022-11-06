push = require '/dependencies/push'
Class = require '/dependencies/class'

require 'Paddle'
require 'Ball'

WINDOW_WIDTH=1280
WINDOW_HEIGHT=720
VIRTUAL_WIDTH=256
VIRTUAL_HEIGHT=256
PADDLE_SPEED=150
START_SCORE=1
ballSpeed=100
paddle1AI=true
paddle2AI=true
paddle3AI=true
paddle4AI=true

function love.load()
    --https://love2d.org/wiki/love.window.setTitle
    love.window.setTitle("Pong | Love2D")
    love.graphics.setDefaultFilter('nearest','nearest')
    smallFont = love.graphics.newFont('/gfx/font.ttf',8)
    largeFont = love.graphics.newFont('/gfx/font.ttf',24)
    push:setupScreen(VIRTUAL_WIDTH,VIRTUAL_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT, {
        fullscreen=false,
        resizable=true,
        vsync=true
    })

    player1 = Paddle(10,30,5,20,paddle1AI,"vert")
    player2 = Paddle(VIRTUAL_WIDTH-10,VIRTUAL_HEIGHT-50,5,20,paddle2AI,"vert")
    player3 = Paddle(30,10,20,5,paddle3AI,"hor")
    player4 = Paddle(VIRTUAL_WIDTH-50,VIRTUAL_HEIGHT-10,20,5,paddle4AI,"hor")
    ball = Ball(VIRTUAL_WIDTH/2-2, VIRTUAL_HEIGHT/2-2,4,4)

    dotState = 0
    gameState = 'start'
    winner = false

    mainMusic = love.audio.newSource("/gfx/loopedMusic.mp3","stream")
    mainMusic:setVolume(0.5)
    hit = love.audio.newSource("/gfx/hit.mp3","static")
    point = love.audio.newSource("/gfx/point.mp3","static")
end

function love.resize(w,h)
    push:resize(w,h)
end

function love.update(dt)
    if not mainMusic:isPlaying() then
		love.audio.play(mainMusic)
	end
    --player 1
    if love.keyboard.isDown('w') and not player1.ele then
        player1.dy = -PADDLE_SPEED
    elseif love.keyboard.isDown('s') and not player1.ele then
        player1.dy = PADDLE_SPEED
    else
        player1.dy = 0
    end
    --player 2
    if love.keyboard.isDown('up') and not player2.ele then
        player2.dy = -PADDLE_SPEED
    elseif love.keyboard.isDown('down') and not player2.ele then
        player2.dy = PADDLE_SPEED
    else
        player2.dy = 0
    end
    --player 3
    if love.keyboard.isDown('g') and not player3.ele then
        player3.dx = -PADDLE_SPEED
    elseif love.keyboard.isDown('t') and not player3.ele then
        player3.dx = PADDLE_SPEED
    else
        player3.dx = 0
    end
    --player 4
    if love.keyboard.isDown('u') and not player4.ele then
        player4.dx = -PADDLE_SPEED
    elseif love.keyboard.isDown('j') and not player4.ele then
        player4.dx = PADDLE_SPEED
    else
        player4.dx = 0
    end
    player1:update(dt)
    player2:update(dt)
    player3:update(dt)
    player4:update(dt)
    if ball:checkCollide(player1) and not player1.ele then
        if ball.DX < 0 then
            ball:collide("vert")
        end
    elseif ball:checkCollide(player2) and not player2.ele then
        if ball.DX > 0 then
            ball:collide("vert")
        end
    elseif ball:checkCollide(player3) and not player3.ele then
        if ball.DY < 0 then
            ball:collide("hor")
        end
    elseif ball:checkCollide(player4) and not player4.ele then
        if ball.DY > 0 then
            ball:collide("hor")
        end
    end
    if gameState == 'play' then
        ball:update(dt)
    end
end

function love.draw()
    push:apply('start')
    --Takes in RGBA value.
    love.graphics.clear(40,45,52,255)
    --Print Main Screen Text
    love.graphics.setFont(smallFont)
    love.graphics.printf("FPS: "..love.timer.getFPS(),0,VIRTUAL_HEIGHT/2-30, VIRTUAL_WIDTH, 'center')
    if gameState == "start" then
        text = loadingAnimation()
        love.graphics.printf("Hit space to begin"..text,0,VIRTUAL_HEIGHT/2-10, VIRTUAL_WIDTH, 'center')
        if winner == "player1" then
            love.graphics.setColor(220,20,60)
            love.graphics.printf("Red has won! Congrats!",0,VIRTUAL_HEIGHT/2-20, VIRTUAL_WIDTH, 'center')
        elseif winner == "player2" then
            love.graphics.setColor(0,191,255)
            love.graphics.printf("Blue has won! Congrats!",0,VIRTUAL_HEIGHT/2-20, VIRTUAL_WIDTH, 'center')
        elseif winner == "player3" then
            love.graphics.setColor(50,205,50)
            love.graphics.printf("Green has won! Congrats!",0,VIRTUAL_HEIGHT/2-20, VIRTUAL_WIDTH, 'center')
        elseif winner == "player4" then
            love.graphics.setColor(255,215,0)
            love.graphics.printf("Yellow has won! Congrats!",0,VIRTUAL_HEIGHT/2-20, VIRTUAL_WIDTH, 'center')
        end
    end
    -- Print Score
    love.graphics.setFont(largeFont)
    --startx, starty, width, height
    --https://love2d.org/forums/viewtopic.php?t=9524
    love.graphics.setColor(220,20,60)
    love.graphics.printf(player1.score.."/"..START_SCORE,-VIRTUAL_WIDTH/2+50,VIRTUAL_HEIGHT/2,VIRTUAL_WIDTH,"center")
    player1:render()
    love.graphics.setColor(0,191,255)
    love.graphics.printf(player2.score.."/"..START_SCORE,VIRTUAL_WIDTH/2-50,VIRTUAL_HEIGHT/2,VIRTUAL_WIDTH,"center")
    player2:render()
    love.graphics.setColor(50,205,50)
    love.graphics.printf(player3.score.."/"..START_SCORE,0,30,VIRTUAL_WIDTH,"center")
    player3:render()
    love.graphics.setColor(255,215,0)
    love.graphics.printf(player4.score.."/"..START_SCORE,0,VIRTUAL_HEIGHT-50,VIRTUAL_WIDTH,"center")
    player4:render()
    love.graphics.setColor(255,255,255)
    ball:render()
    push:apply('end')
end

function love.keypressed(key)
    if key == 'escape' then
        love.event.quit()
    elseif key == "space" then
        gameStateChange()
    end
end

function loadingAnimation(num)
    if dotState < 1 then
        text = "."
    elseif dotState < 2 then
        text = ".."
    elseif dotState < 3 then
        text = "..."
    end
    dotState=dotState+0.01
    if dotState > 3 then
        dotState = 0
    end
    return text
end

function gameStateChange()
    if gameState == 'start' then
        gameState = 'play'
        winner = false
    elseif gameState == 'play' then
        gameState = 'start'
        ball:reset()
    end
end

function gameReset()
    player1.score = START_SCORE
    player2.score = START_SCORE
    player3.score = START_SCORE
    player4.score = START_SCORE
    player1.ele = false
    player2.ele = false
    player3.ele = false
    player4.ele = false
    gameState = "start"
end

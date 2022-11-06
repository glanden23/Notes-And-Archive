push = require '/dependencies/push'
Class = require '/dependencies/class'

require 'Paddle'
require 'Ball'

WINDOW_WIDTH=1280
WINDOW_HEIGHT=720
VIRTUAL_WIDTH=432
VIRTUAL_HEIGHT=243
PADDLE_SPEED=150
MAX_SCORE=3
ballSpeed=100
paddle1AI=true
paddle2AI=true

function love.load()
    --https://love2d.org/wiki/love.window.setTitle
    love.window.setTitle("Pong | Love2D")
    love.graphics.setDefaultFilter('nearest','nearest')
    smallFont = love.graphics.newFont('/gfx/font.ttf',8)
    largeFont = love.graphics.newFont('/gfx/font.ttf',24)
    push:setupScreen(VIRTUAL_WIDTH,VIRTUAL_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT, {
        fullscreen=false,
        resizable=false,
        vsync=true
    })
    player1 = Paddle(10,30,5,20,paddle1AI)
    player2 = Paddle(VIRTUAL_WIDTH-10,VIRTUAL_HEIGHT-50,5,20,paddle2AI)
    ball = Ball(VIRTUAL_WIDTH/2-2, VIRTUAL_HEIGHT/2-2,4,4)

    dotState = 0
    gameState = 'start'
    winner = false

    ballType = "Normal"

    mainMusic = love.audio.newSource("/gfx/loopedMusic.mp3","stream")
    mainMusic:setVolume(0.5)
    hit = love.audio.newSource("/gfx/hit.mp3","static")
    point = love.audio.newSource("/gfx/point.mp3","static")
end

function love.update(dt)
    if not mainMusic:isPlaying() then
		love.audio.play(mainMusic)
	end
    --player 1
    if love.keyboard.isDown('w') then
        player1.dy = -PADDLE_SPEED
    elseif love.keyboard.isDown('s') then
        player1.dy = PADDLE_SPEED
    else
        player1.dy = 0
    end
    --player 2
    if love.keyboard.isDown('up') then
        player2.dy = -PADDLE_SPEED
    elseif love.keyboard.isDown('down') then
        player2.dy = PADDLE_SPEED
    else
        player2.dy = 0
    end
    player1:update(dt)
    player2:update(dt)
    if ball:checkCollide(player1) then
        if ball.DX == -100 then
            if love.math.random(2) == 2 then
                ball:changeMode()
            end
            ball:collide()
        end
    elseif ball:checkCollide(player2) then
        if ball.DX == 100 then
            if love.math.random(2) == 2 then
                ball:changeMode()
            end
            ball:collide()
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
    love.graphics.setColor(50,205,50)
    love.graphics.printf("FPS: "..love.timer.getFPS(),0,0, VIRTUAL_WIDTH, 'center')
    love.graphics.printf("Ball Type: "..ballType,0,10, VIRTUAL_WIDTH, 'center')
    if gameState == "start" then
        love.graphics.setColor(255,255,0)
        text = loadingAnimation()
        love.graphics.printf("Hit space to begin"..text,0,60, VIRTUAL_WIDTH, 'center')
        if winner == "blue" then
            love.graphics.setColor(0,191,255)
            love.graphics.printf("Blue has won! Congrats!",0,90, VIRTUAL_WIDTH, 'center')
        elseif winner == "red" then
            love.graphics.setColor(220,20,60)
            love.graphics.printf("Red has won! Congrats!",0,90, VIRTUAL_WIDTH, 'center')
        end
    end
    if not winner == false then
        if player1.score > 5 then
            winner = "blue"
        else
            winner = "red"
        end
    end
    -- Print Score
    love.graphics.setFont(largeFont)
    --startx, starty, width, height
    --https://love2d.org/forums/viewtopic.php?t=9524
    love.graphics.setColor(220,20,60)
    love.graphics.printf(player1.score.."/"..MAX_SCORE,50,0,VIRTUAL_WIDTH,"left")
    player1:render()
    love.graphics.setColor(0,191,255)
    love.graphics.printf(player2.score.."/"..MAX_SCORE,-50,0,VIRTUAL_WIDTH,"right")
    player2:render()
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
    player1.score = 0
    player2.score = 0
    gameStateChange()
end

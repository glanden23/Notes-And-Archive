--var = import or require the file push
push = require 'push'

WINDOW_WIDTH=1280
WINDOW_HEIGHT=720
VIRTUAL_WIDTH=432
VIRTUAL_HEIGHT=243
PADDLE_SPEED=200

function love.load()
    love.graphics.setDefaultFilter('nearest','nearest')
    smallFont = love.graphics.newFont('font.ttf',8)
    largeFont = love.graphics.newFont('font.ttf',32)
    push:setupScreen(VIRTUAL_WIDTH,VIRTUAL_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT, {
        fullscreen=false,
        resizable=false,
        vsync=true
    })
    player1Y = 30
    player1X = 10
    player2Y = VIRTUAL_HEIGHT-50
    player2X = VIRTUAL_WIDTH-10

    ballX = VIRTUAL_WIDTH/2-2
    ballY = VIRTUAL_HEIGHT/2-2
    ballDX = 0
    ballDY = 0
    dotState = 0

    gameState = 'start'
end

function love.update(dt)
    --player 1
    if love.keyboard.isDown('w') and player1Y > 0 then
        player1Y = player1Y + -PADDLE_SPEED * dt
    elseif love.keyboard.isDown('s') and player1Y < VIRTUAL_HEIGHT-20 then
        player1Y = player1Y + PADDLE_SPEED * dt
    end
    --player 2
    if love.keyboard.isDown('up') and player2Y > 0 then
        player2Y = player2Y + -PADDLE_SPEED * dt
    elseif love.keyboard.isDown('down') and player2Y < VIRTUAL_HEIGHT-20 then
        player2Y = player2Y + PADDLE_SPEED * dt
    end
    ballX = ballX + ballDX * dt
    ballY = ballY + ballDY * dt
end

function love.draw()
    push:apply('start')
    --Takes in RGBA value.
    love.graphics.clear(40,45,52,255)
    --Print Main Screen Text
    love.graphics.setFont(smallFont)
    love.graphics.setColor(50,205,50)
    love.graphics.printf("Current FPS: "..love.timer.getFPS(),0,0, VIRTUAL_WIDTH, 'center')
    if gameState == "start" then
        love.graphics.setColor(255,255,0)
        if dotState < 1 then text = "." elseif dotState < 2 then text = ".." else text = "..." end
        dotState=dotState+0.03
        if dotState > 3 then
            dotState = 0
        end
        love.graphics.printf("Hit space when you to begin!\n"..text,0,60, VIRTUAL_WIDTH, 'center')
    end
    -- Print Score
    love.graphics.setFont(largeFont)
    --startx, starty, width, height
    --https://love2d.org/forums/viewtopic.php?t=9524
    love.graphics.setColor(220,20,60)
    love.graphics.printf("0",50,0,VIRTUAL_WIDTH,"left")
    love.graphics.rectangle('fill',player1X,player1Y,5,20)
    love.graphics.setColor(0,191,255)
    love.graphics.printf("0",-50,0,VIRTUAL_WIDTH,"right")
    love.graphics.rectangle('fill',player2X,player2Y,5,20)
    love.graphics.setColor(255,255,255)
    love.graphics.rectangle('fill',ballX,ballY,4,4)
    push:apply('end')
end

function gameStateChange()
    if gameState == 'start' then
        gameState = 'play'
        ballDX = love.math.random(2) < 2 and 100 or -100
        ballDY = love.math.random(-80, 80)
    elseif gameState == 'play' then
        gameState = 'start'
        ballX = VIRTUAL_WIDTH/2-2
        ballY = VIRTUAL_HEIGHT/2-2
        ballDX = 0
        ballDY = 0
    end
end

function love.keypressed(key)
    if key == 'escape' then
        love.event.quit()
    elseif key == "space" then
        gameStateChange()
    end
end
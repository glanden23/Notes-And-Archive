push = require 'push'
Class = require 'class'

WINDOW_WIDTH=1280
WINDOW_HEIGHT=720
VIRTUAL_WIDTH=432
VIRTUAL_HEIGHT=243

function love.load()
    love.window.setTitle("Clock | Love2D")
    love.graphics.setDefaultFilter('nearest','nearest')
    font = love.graphics.newFont('font.ttf',32)
    push:setupScreen(VIRTUAL_WIDTH,VIRTUAL_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT, {
        fullscreen=false,
        resizable=true,
        vsync=true
    })
end

function love.resize(w,h)
    push:resize(w,h)
end

function love.update(dt)
    --https://love2d.org/forums/viewtopic.php?t=881
    time = os.date('*t')
end

function love.draw()
    push:apply('start')
    --https://love2d.org/forums/viewtopic.php?t=87378
    if string.len(tostring(time.min)) < 2 then
        time.min = "0"..time.min
    end
    if string.len(tostring(time.sec)) < 2 then
        time.sec = "0"..time.sec
    end
    love.graphics.setFont(font)
    love.graphics.printf(time.month.."/"..time.day.."/"..time.year.."\n"..time.hour..":"..time.min..":"..time.sec,0,0,VIRTUAL_WIDTH,"center")
    push:apply('end')
end

function love.keypressed(key)
    if key == 'escape' then
        love.event.quit()
    end
end
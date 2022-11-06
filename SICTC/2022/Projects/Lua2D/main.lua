push = require '/depend/push'
Class = require '/depend/class'

require("/modules/blocks")
require("/modules/generator")
require("/depend/myjunk")
require("/modules/character")
require("blockList")

WINDOW_WIDTH=720
WINDOW_HEIGHT=720
VIRTUAL_WIDTH=310
VIRTUAL_HEIGHT=310
BLOCK_SIZE=1
LOAD_DISTANCE=BLOCK_SIZE
blocks = {}

function love.load()
    love.window.setTitle("Love 2'd | Love2D")
    love.graphics.setDefaultFilter('nearest','nearest')
    smallFont = love.graphics.newFont('/depend/font.ttf',8)
    largeFont = love.graphics.newFont('/depend/font.ttf',24)
    push:setupScreen(VIRTUAL_WIDTH,VIRTUAL_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT, {
        fullscreen=false,
        resizable=true,
        vsync=true
    })
    character = Character()
    currBack=love.graphics.newImage('/gfx/forest.png')
    love.keyboard.setKeyRepeat(true)
end

function love.resize(w,h)
    push:resize(w,h)
end
local update = 0
function love.update(dt)
    genCheckChunk()
    for i in pairs(blocks) do
        blocks[i]:clearMem(i)
    end
    update=update+(dt*100)
    if update > 1 then
        moveBlocks(-1)
        update=0
    end
end

backMov = 0

function love.draw()
    backMov=backMov-0.05
    if -currBack:getWidth()+(VIRTUAL_WIDTH*3) > backMov then
        backMov=0
    end
    love.graphics.draw(currBack, backMov)
    push:apply('start')
    --Render debug
    love.graphics.setFont(smallFont)
    --love.graphics.printf("Blocks: "..tablelen(blocks),0,0, VIRTUAL_WIDTH, 'left')
    love.graphics.printf("FPS: "..love.timer.getFPS(),0,0, VIRTUAL_WIDTH, 'right')
    --love.graphics.setColor(1,1,1,1)      
    for i in pairs(blocks) do
        blocks[i]:render()
    end
    if love.timer.getFPS() < 10 then
        blocks={}
        BLOCK_SIZE=BLOCK_SIZE+1
    end
    push:apply('end')
end

function love.keypressed(key)
    if key == 'escape' then
        love.event.quit()
    end
    --character:move(key)
end

updateScreen = 0
function updateMove(dt)
    if updateScreen > 0.1 then
        moveBlocks(-1) 
        updateScreen=0
    end
    updateScreen=updateScreen+(10*dt)
end
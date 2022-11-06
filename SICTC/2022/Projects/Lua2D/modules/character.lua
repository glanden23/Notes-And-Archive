Character = Class{}

-- Constructor
function Character:init(speed)
    self.x=VIRTUAL_WIDTH/2
    self.y=VIRTUAL_HEIGHT/2
end

function Character:render()
    --love.graphics.setColor( red, green, blue, alpha )
    love.graphics.setColor(138,121,93)
    --love.graphics.rectangle( mode, x, y, width, height, rx, ry, segments )
    love.graphics.rectangle("fill", self.x,self.y,BLOCK_SIZE,BLOCK_SIZE)
end

function Character:update()
end

function Character:move(key)
    if key == "right" then
        moveBlocks(-1)
    elseif key == "left" then
        moveBlocks(1)
    end
end

function moveBlocks(neg)
    for i in pairs(blocks) do
        blocks[i]:move(neg*BLOCK_SIZE,"x")
    end
end

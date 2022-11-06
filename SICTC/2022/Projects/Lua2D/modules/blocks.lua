Block = Class{}

-- Constructor
function Block:init(x,y,type,surface)
    self.type = type
    if surface == nil then
        self.surface = false
    else
        self.surface = surface
    end
    for i in pairs(blockList) do
        if blockList[i][1] == type then
            self.color = blockList[i][2]
        end
    end
    self.x = x
    self.y = y
end

function Block:render()
    --love.graphics.setColor( red, green, blue, alpha )
    love.graphics.setColor(self.color[1], self.color[2], self.color[3], self.color[4])
    --love.graphics.rectangle( mode, x, y, width, height, rx, ry, segments )
    love.graphics.rectangle("fill", self.x,self.y,BLOCK_SIZE,BLOCK_SIZE)
end

function Block:move(BLOCK_SIZE)
    self.x = self.x+BLOCK_SIZE
end

function Block:clearMem(i)
    if self.x > VIRTUAL_WIDTH+LOAD_DISTANCE or self.x < -LOAD_DISTANCE then
        table.remove(blocks,i)
    end
end
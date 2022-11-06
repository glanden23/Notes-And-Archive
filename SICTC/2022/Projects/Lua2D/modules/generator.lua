currBiome = 0

local minLastGen=0

function genCheckChunk()
    local x = 0
    while x < VIRTUAL_WIDTH do
        local found = 0
        for i in pairs(blocks) do
            if blocks[i].x == x and blocks[i].surface then
                found = found+1
                break
            end
        end
        if found == 0 then
            local lastY = genGetLastHeight(x)
            minLastGen=minLastGen+1
            print(minLastGen)
            if love.math.random(0,100) == 0 and minLastGen > 500 then
                backMov=0
                minLastGen=0
                local oldBiome = currBiome
                currBiome = love.math.random(0,0)
                if currBiome == 0 then
                    currBack=love.graphics.newImage('/gfx/forest.png')
                elseif currBiome == 1 then
                    currBack=love.graphics.newImage('/gfx/ice.png')
                elseif currBiome == 2 then
                    currBack=love.graphics.newImage('/gfx/mountain.png')
                end
            end
            if currBiome == 0 then
                genForest(x, lastY)
            elseif currBiome == 1 then
                genIceForest(x, lastY)
            else
                genDesert(x,lastY)
            end
        end
        x=x+BLOCK_SIZE
    end
end

function genGetLastHeight(x)
    for i in pairs(blocks) do
        if blocks[i].surface and blocks[i].x-BLOCK_SIZE == x then
            return blocks[i].y
        elseif blocks[i].surface and blocks[i].x+BLOCK_SIZE == x then
            return blocks[i].y
        end
    end
    return love.math.random(0,VIRTUAL_HEIGHT)
end

local currDir=0
local cDirThres=0
function genForest(x, lastY)
    lastY = heightVary(lastY, 50, 5)
    genTree(x,lastY-BLOCK_SIZE)
    table.insert(blocks,1,Block(x,lastY,"Grass",true))
    local genSur=3
    while lastY < VIRTUAL_HEIGHT do
        if genSur > 0 then
            table.insert(blocks,1,Block(x,lastY,"Dirt"))
            genSur=genSur-1
        else
            table.insert(blocks,1,Block(x,lastY,"Stone"))
        end
        lastY=lastY+BLOCK_SIZE
    end
end

function genIceForest(x, lastY)
    lastY = heightVary(lastY, 50, 5)
    genIceTree(x,lastY-BLOCK_SIZE)
    table.insert(blocks,1,Block(x,lastY,"Snow",true))
    local genSur=3
    while lastY < VIRTUAL_HEIGHT do
        if genSur > 0 then
            table.insert(blocks,1,Block(x,lastY,"Ice"))
            genSur=genSur-1
        else
            table.insert(blocks,1,Block(x,lastY,"Stone"))
        end
        lastY=lastY+BLOCK_SIZE
    end
end

function genDesert(x, lastY)
    lastY = heightVary(lastY, 50, 5)
    genCac(x,lastY-BLOCK_SIZE)
    table.insert(blocks,1,Block(x,lastY,"Sand",true))
    local genSur=3
    while lastY < VIRTUAL_HEIGHT do
        if genSur > 0 then
            table.insert(blocks,1,Block(x,lastY,"Sand"))
            genSur=genSur-1
        else
            table.insert(blocks,1,Block(x,lastY,"Sandstone"))
        end
        lastY=lastY+BLOCK_SIZE
    end
end

function heightVary(lastY, highest, lowest)
    if cDirThres >= 3 or lastY < (BLOCK_SIZE*highest) then
        currDir=1
        cDirThres=0
    elseif cDirThres <= -3 or lastY > VIRTUAL_HEIGHT-(BLOCK_SIZE*lowest) then
        currDir=0
        cDirThres=0
    end
    cDirThres=cDirThres+love.math.random(-1,1)
    if currDir == 1 and love.math.random(0,1) == 0 then
        lastY=lastY+BLOCK_SIZE
        lastDir=0
    elseif currDir == 0 and love.math.random(0,1) == 0 then
        lastY=lastY-BLOCK_SIZE
        lastDir=0
    end
    return lastY
end

tCLT = 0
tCLTM = love.math.random(3,25)
function genTree(x,y)
    if tCLT < tCLTM then
        tCLT=tCLT+1
        return
    end
    tCLT=0
    tCLTM=love.math.random(3,25)
    table.insert(blocks,1,Block(x,y,"Wood"))
    table.insert(blocks,1,Block(x,y-BLOCK_SIZE,"Wood"))
    table.insert(blocks,1,Block(x,y-BLOCK_SIZE*2,"Wood"))
    table.insert(blocks,1,Block(x,y-BLOCK_SIZE*3,"Leaves"))
    table.insert(blocks,1,Block(x-BLOCK_SIZE,y-BLOCK_SIZE*3,"Leaves"))
    table.insert(blocks,1,Block(x+BLOCK_SIZE,y-BLOCK_SIZE*3,"Leaves"))
    table.insert(blocks,1,Block(x,y-BLOCK_SIZE*4,"Leaves"))
    table.insert(blocks,1,Block(x-BLOCK_SIZE,y-BLOCK_SIZE*4,"Leaves"))
    table.insert(blocks,1,Block(x+BLOCK_SIZE,y-BLOCK_SIZE*4,"Leaves"))
    table.insert(blocks,1,Block(x,y-BLOCK_SIZE*5,"Leaves"))
    table.insert(blocks,1,Block(x-BLOCK_SIZE,y-BLOCK_SIZE*5,"Leaves"))
    table.insert(blocks,1,Block(x+BLOCK_SIZE,y-BLOCK_SIZE*5,"Leaves"))
end

function genIceTree(x,y)
    if tCLT < tCLTM then
        tCLT=tCLT+1
        return
    end
    tCLT=0
    tCLTM=love.math.random(3,25)
    table.insert(blocks,1,Block(x,y,"Wood"))
    table.insert(blocks,1,Block(x,y-BLOCK_SIZE,"Wood"))
    table.insert(blocks,1,Block(x,y-BLOCK_SIZE*2,"Wood"))
    table.insert(blocks,1,Block(x,y-BLOCK_SIZE*3,"Ice"))
    table.insert(blocks,1,Block(x-BLOCK_SIZE,y-BLOCK_SIZE*3,"Ice"))
    table.insert(blocks,1,Block(x+BLOCK_SIZE,y-BLOCK_SIZE*3,"Ice"))
    table.insert(blocks,1,Block(x,y-BLOCK_SIZE*4,"Ice"))
    table.insert(blocks,1,Block(x-BLOCK_SIZE,y-BLOCK_SIZE*4,"Ice"))
    table.insert(blocks,1,Block(x+BLOCK_SIZE,y-BLOCK_SIZE*4,"Ice"))
    table.insert(blocks,1,Block(x,y-BLOCK_SIZE*5,"Ice"))
    table.insert(blocks,1,Block(x-BLOCK_SIZE,y-BLOCK_SIZE*5,"Ice"))
    table.insert(blocks,1,Block(x+BLOCK_SIZE,y-BLOCK_SIZE*5,"Ice"))
end

function genCac(x,y)
    if tCLT < tCLTM then
        tCLT=tCLT+1
        return
    end
    tCLT=0
    tCLTM=love.math.random(3,25)
    table.insert(blocks,1,Block(x,y,"Cactus"))
    table.insert(blocks,1,Block(x,y-BLOCK_SIZE,"Cactus"))
    table.insert(blocks,1,Block(x,y-BLOCK_SIZE*2,"Cactus"))
    table.insert(blocks,1,Block(x,y-BLOCK_SIZE*3,"Cactus"))
    table.insert(blocks,1,Block(x-BLOCK_SIZE,y-BLOCK_SIZE*3,"Cactus"))
    table.insert(blocks,1,Block(x+BLOCK_SIZE,y-BLOCK_SIZE*3,"Cactus"))
end

--TODO
function genCloud(x,y)
    local cloud = {255,255,255,255}
    while y > -BLOCK_SIZE do
        table.insert(blocks,1,Block(x,y,true,cloud))
        y=y-BLOCK_SIZE
    end
end

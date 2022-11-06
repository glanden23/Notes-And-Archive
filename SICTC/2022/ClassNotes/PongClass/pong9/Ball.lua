Ball = Class{}

-- Constructor
function Ball:init(x,y,w,h)
    self.startx = x
    self.starty = y
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.DX = love.math.random(2) < 2 and ballSpeed or -ballSpeed
    self.DY = love.math.random(-80, 80)
end

-- Update
function Ball:update(dt)
    self.x = self.x + self.DX * dt
    self.y = self.y + self.DY * dt
    if self.x > VIRTUAL_WIDTH then
        ball:reset()
        player1:addScore()
        point:play()
    elseif self.x < 0 then
        ball:reset()
        player2:addScore()
        point:play()
    end
    if self.y > VIRTUAL_HEIGHT then
        self.DY = -self.DY + love.math.random(-25,25)
        self.y = self.y - 2
    elseif self.y < 0 then
        self.DY = -self.DY + love.math.random(-25,25)
        self.y = self.y + 2
    end
end

function Ball:checkCollide(paddle)
    if self.x > paddle.x + paddle.w or paddle.x > self.x + self.w then
        return false
    end
    if self.y > paddle.y + paddle.h or paddle.y > self.y + self.h then
        return false
    end
    return true
end

-- Draw or render
function Ball:render()
    love.graphics.rectangle('fill',self.x,self.y,self.w,self.h)
    if gameState == "start" then
        if self.DX < 0 then
            serve = "Left"
        else
            serve = "Right"
        end
        love.graphics.setFont(smallFont)
        love.graphics.printf("Serving to "..serve.."!",0,40, VIRTUAL_WIDTH, 'center')
    end
end

function Ball:collide()
    hit:play()
    --https://love2d.org/forums/viewtopic.php?t=75939
    self.DX = -self.DX
    if ballType == "Random" then
        self.DY = self.DY + love.math.random(-150, 150)
    elseif ballType == "Shooter" then
        self.DY = self.DY + love.math.random(-10, 10)
        self.y = love.math.random(0, VIRTUAL_HEIGHT)
    elseif ballType == "Bouncer" then
        self.DY = love.math.random(2) < 2 and 100 or -100
    else
        self.DY = self.DY + love.math.random(-10, 10)
    end
end

function Ball:changeMode()
    ballType = love.math.random(6)
    if ballType == 1 then
        ballType = "Random"
    elseif ballType == 2 then
        ballType = "Shooter"
    elseif ballType == 3 then
        ballType = "Bouncer"
    else
        ballType = "Normal"
        self.DY = love.math.random(-50, 50)
    end
end

function Ball:reset()
    ballSpeed=100
    self.DX = love.math.random(2) < 2 and ballSpeed or -ballSpeed
    self.DY = love.math.random(-50, 50)
    self.x = self.startx
    self.y = self.starty
end
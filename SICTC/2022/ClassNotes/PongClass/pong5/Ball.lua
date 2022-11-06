Ball = Class{}

-- Constructor
function Ball:init(x,y)
    self.startx = x
    self.starty = y
    self.x = x
    self.y = y
    self.DX = love.math.random(2) < 2 and BALL_SPEED or -BALL_SPEED
    self.DY = love.math.random(-80, 80)
end

-- Update
function Ball:update(dt)
    self.x = self.x + self.DX * dt
    self.y = self.y + self.DY * dt
    if self.x > VIRTUAL_WIDTH then
        ball:reset()
    elseif self.x < 0 then
        ball:reset()
    end
    if self.y > VIRTUAL_HEIGHT then
        self.DY = -self.DY + love.math.random(-10,10)
    elseif self.y < 0 then
        self.DY = -self.DY + love.math.random(-10,10)
    end
end

-- Draw or render
function Ball:render()
    love.graphics.rectangle('fill',self.x,self.y,4,4)
end

function Ball:collide()
    --https://love2d.org/forums/viewtopic.php?t=75939
    if self.DX == BALL_SPEED then
        self.DX = -BALL_SPEED
    else
        self.DX = BALL_SPEED
    end
end

function Ball:reset()
    self.DX = love.math.random(2) < 2 and BALL_SPEED or -BALL_SPEED
    self.DY = love.math.random(-50, 50)
    self.x = self.startx
    self.y = self.starty
end
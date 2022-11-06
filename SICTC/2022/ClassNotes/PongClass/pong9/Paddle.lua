Paddle = Class{}

-- Constructor
function Paddle:init(x,y,width,height,ai)
    self.x = x
    self.y = y
    self.w = width
    self.h = height
    self.ai = ai
    self.dy = 0
    self.score = 0
end

-- Update
function Paddle:update(dt)
    if self.dy < 0 then
        self.y = math.max(0, self.y + self.dy * dt)
    else
        self.y = math.min(VIRTUAL_HEIGHT-self.h,self.y + self.dy * dt)
    end
    if self.ai then
        self.y = ball.y-self.h/2
    end
end

function Paddle:addScore()
    self.score = self.score+1
    if self.score == MAX_SCORE then
        winner=true
        gameReset()
    end
end

-- Draw or render
function Paddle:render()
    love.graphics.rectangle('fill',self.x,self.y,self.w,self.h)
end
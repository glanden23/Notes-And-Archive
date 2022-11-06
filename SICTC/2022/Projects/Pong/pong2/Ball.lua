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
    self.DY = love.math.random(2) < 2 and ballSpeed or -ballSpeed
end

-- Update
function Ball:update(dt)
    self.x = self.x + self.DX * dt
    self.y = self.y + self.DY * dt
    if self.x > VIRTUAL_WIDTH then
        if player2.ele then
            self.DX = -self.DX
            return
        end
        ball:reset("2")
        player2:removeScore()
        point:play()
    elseif self.x < 0 then
        if player1.ele then
            self.DX = -self.DX
            return
        end
        ball:reset("1")
        player1:removeScore()
        point:play()
    elseif self.y > VIRTUAL_HEIGHT then
        if player4.ele then
            self.DY = -self.DY
            return
        end
        ball:reset("4")
        player4:removeScore()
        point:play()
    elseif self.y < 0 then
        if player3.ele then
            self.DY = -self.DY
            return
        end
        ball:reset("3")
        player3:removeScore()
        point:play()
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
        serve = ""
        if self.DX < 0 then
            serve = serve.."Left"
        else
            serve = serve.."Right"
        end
        if self.DY < 0 then
            serve = serve.." Up"
        else
            serve = serve.." Down"
        end
        love.graphics.setFont(smallFont)
        love.graphics.printf("Serving to "..serve.."!",0,VIRTUAL_HEIGHT/2-20, VIRTUAL_WIDTH, 'center')
    end
end

function Ball:collide(collide)
    hit:play()
    --https://love2d.org/forums/viewtopic.php?t=75939
    if collide == "vert" then
        self.DX = -self.DX + love.math.random(-15, 15)
        self.DY = self.DY + love.math.random(-15, 15)
    else
        self.DX = self.DX + love.math.random(-15, 15)
        self.DY = -self.DY + love.math.random(-15, 15)
    end
end

function Ball:reset(scorer)
    self.DX = love.math.random(2) < 2 and ballSpeed or -ballSpeed
    self.DY = love.math.random(2) < 2 and ballSpeed or -ballSpeed
    if scorer == "1" then
        self.x = player1.x
        self.y = player1.y
    elseif scorer == "2" then
        self.x = player2.x
        self.y = player2.y
    elseif scorer == "3" then
        self.x = player3.x
        self.y = player3.y
    else
        self.x = player4.x
        self.y = player4.y
    end
end
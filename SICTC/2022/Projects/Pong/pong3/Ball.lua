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
    if mode == "Flutter" then
        if self.DY > 100 or self.DX > 100 then
            self.DY = self.DY - 3
            self.DX = self.DX - 3
        elseif self.DY < -100 or self.DX < -100 then
            self.DY = self.DY + 3
            self.DX = self.DX + 3
        else
            self.DY = self.DY + (love.math.random(0, 1) < 1 and -3 or 3)
            self.DX = self.DX + (love.math.random(0, 1) < 1 and -3 or 3)
        end
    end
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

function Ball:collide(collide,user)
    hit:play()
    --https://love2d.org/forums/viewtopic.php?t=75939
    if mode == "Shooter" then
        self:Shooter(user)  
    elseif mode == "Random" then
        self.DX = (love.math.random(0,1) < 1 and -100 or 100) + love.math.random(-15, 15)
        self.DY = (love.math.random(0,1) < 1 and -100 or 100) + love.math.random(-15, 15)
    else
        if collide == "vert" then
            self.DX = -self.DX + love.math.random(-15, 15)
            self.DY = self.DY + love.math.random(-15, 15)
        else
            self.DX = self.DX + love.math.random(-15, 15)
            self.DY = -self.DY + love.math.random(-15, 15)
        end
    end
    self:changemode()
end

function Ball:reset(scorer)
    if mode == "Shooter" then
        self:Shooter()
    else
        self.DX = love.math.random(2) < 2 and ballSpeed or -ballSpeed
        self.DY = love.math.random(2) < 2 and ballSpeed or -ballSpeed
    end
    if scorer == "1" then
        self.x = player1.x
        self.y = player1.y
    elseif scorer == "2" then
        self.x = player2.x
        self.y = player2.y
    elseif scorer == "3" then
        self.x = player3.x
        self.y = player3.y
    elseif scorer == "4" then
        self.x = player4.x
        self.y = player4.y
    else
        mode = "Normal"
        self.x = VIRTUAL_WIDTH/2
        self.y = VIRTUAL_HEIGHT/2
    end
end

function Ball:Shooter(user)
    if user == nil then
        return
    end
    if user.type == "vert" then
        self.DX = love.math.random(0,1) < 1 and -200 or 200
        self.DY = 0
        local y = love.math.random(0+100, VIRTUAL_HEIGHT-100)
        user.y = y
        self.y = y
    else
        self.DY = love.math.random(0,1) < 1 and -200 or 200
        self.DX = 0
        local x = love.math.random(0+100, VIRTUAL_WIDTH-100)
        user.x = x
        self.x = x
    end 
end

function Ball:changemode()
    if love.math.random(0, 15) == 0 then        
        self.DX = love.math.random(2) < 2 and ballSpeed or -ballSpeed
        self.DY = love.math.random(2) < 2 and ballSpeed or -ballSpeed
        if mode == "Normal" then
            local n = love.math.random(0,2)
            if n == 0 then
                self:Shooter()
                mode = "Shooter"
            elseif n == 2 then
                mode = "Flutter"
            else
                mode = "Random"
            end
        else
            mode = "Normal"
        end
    end
end
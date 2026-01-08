-- step 1: get the local speed vector of the vehicle
-- step 2: take the z coordinate (outputs forward/backward speed)
-- step 3: multiply by -1 to get inverse of forward/back vector magintude
-- step 4: pass to propulsion system
-- WORKING V1.0 BUT I'd like to get it working automatically

function Update(I)
    --do all of this only if we are letting AI control propulsion
        if (I:GetPropulsionRequest(2) > 0) then --if tertiary engaged at all
            I:LogToHud("Brakes ON")
            fwdVelocity = I:GetForwardsVelocityMagnitude()
            counterVelocity = fwdVelocity * -1
            -- here's where we might want to scale it
            -- now we add propulsion request to fwd/back with this value
            I:AddPropulsionRequest(0, counterVelocity) -- 0 for main drive, then send in our counter force
        else
            I:LogToHud("Brakes OFF")
            I:TellAiThatWeAreTakingControl()
        end
end

--trimmed version

function Update(I)
        if (I:GetPropulsionRequest(2) > 0) then
            I:LogToHud("Brakes ON")
            fwdVelocity = I:GetForwardsVelocityMagnitude()
            counterVelocity = fwdVelocity * -1
            I:AddPropulsionRequest(0, counterVelocity)
        else
            I:LogToHud("Brakes OFF")
            I:TellAiThatWeAreTakingControl()
        end
end
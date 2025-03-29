-- NameScan will return the index of the friendly containing the given text string
function NameScan(I, nameString)

    -- number of friendlies on the field
    local friendlyCount = I:GetFriendlyCount()
    -- index of the friendly with nameString in its name
    local targetConstructIndex = -1

    -- for each friendly in the list...
    for index = 0, friendlyCount - 1 do
        --get the FriendlyInfo object of the friendly at index
        local friendlyInfo = I:GetFriendlyInfo(index)
        --get the name of the friendly
        local friendlyName = friendlyInfo.BlueprintName
        --trim the string of the name down to the length of nameString
        local trimName = string.sub(friendlyName, 1, 14)

        I:Log(string.format("Friendly Name %s - Trim Name %s", friendlyName, trimName))

        --if they are equal now, we have our target.
        if trimName == nameString and friendlyInfo.Valid then
            --idk which one it should be here
            targetConstructIndex = friendlyInfo.Id
            targetConstructIndex = index
        end
        --this function should return the unique id of this friendly found above
    end -- close for loop
    return targetConstructIndex
end -- close function

function Update(I)
    I:Log("-START-")
    --loop through all tractor beams on the construct
    local tractorBeamCount = I:Component_GetCount(7)
    I:Log("BeamCount="..tractorBeamCount)
    for i = 0, tractorBeamCount, 1 do
        --get the Shift+N name of the current tractor beam
        local tbInfo = I:Component_GetBlockInfo(7,i)
        local tbName = tbInfo.CustomName

        -- if we have a Target Set, bind this tractor beam to the first TS construct friendly
        if tbName == "Target Set" then
            I:Log("Target Set Beam")
            --search through the list of friendly constructs
            --find one with "Target Set" in the name
            local beamTargetIndex = NameScan(I, "Target Set")
            --if -1 is returned, nothing to be done
            if beamTargetIndex == -1 then
                I:Log("No TS Found")
            end
            --tell this tractor beam to grab it
            I:Component_SetIntLogic_1(7, i, 0, beamTargetIndex)
            --type=7 for tractor beam
            --blockIndex= index of the tractor beam we're working with
            --propertyIndex1=index of the component you want to set int logic for
            --int=the number you want to set the property to

        end
        if tbName == "Weapon" then
            I:Log("Weapon Beam")
        else
            I:Log("oh god, forget it")
        end
        --I:Log(tbName)
    end
end
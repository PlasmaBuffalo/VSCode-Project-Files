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
        --I:Log(string.format("nameString=%s, length=%d", nameString, string.len(nameString)))
        local trimName = string.sub(friendlyName, 1, string.len(nameString))

        --I:Log(string.format("Friendly Name %s - Trim Name %s", friendlyName, trimName))

        --if they are equal now, we have our target.
        I:Log(string.format("Comparing %s and %s", trimName, nameString))
        if trimName == nameString and friendlyInfo.Valid then
            I:Log(string.format("Confirmed match between %s and %s", trimName, nameString))
            --idk which one it should be here
            targetConstructIndex = friendlyInfo.Id
            --targetConstructIndex = index
            return targetConstructIndex
        end
        --this function should return the unique id of this friendly found above
    end -- close for loop
    --this return should only ever return -1
    I:Log("Returning "..targetConstructIndex)
    return targetConstructIndex
end -- close function

function Update(I)
    I:Log("-START-")
    --loop through all tractor beams on the construct
    local tractorBeamCount = I:Component_GetCount(7)
    I:Log("BeamCount="..tractorBeamCount)
    for i = 0, tractorBeamCount, 1 do
        --get the custom name of the current tractor beam
        local beamInfo = I:Component_GetBlockInfo(7,i)
        local beamName = beamInfo.CustomName

        -- if we have a Target Set, bind this tractor beam to the first TS construct friendly
        if beamName == "Target Set" then
            --I:Log("Target Set Beam")
            --search through the list of friendly constructs
            --find one with "Target Set" in the name
            local beamTargetIndex = NameScan(I, "PTP Target Set")
            --tell this tractor beam to grab
            I:Component_SetIntLogic_1(7, i, 0, beamTargetIndex)
            I:Log(string.format("Set component type %d"))
            --type=7 for tractor beam
            --blockIndex= index of the tractor beam we're working with
            --propertyIndex1=index of the component you want to set int logic for
            --int=the number you want to set the property to

        elseif beamName == "Weapon" then
            --I:Log("Weapon Beam")
            --search through the list of friendly constructs
            --find one with "Weapon" in the name
            local beamTargetIndex = NameScan(I, "PTP Weapon")
            --tell this tractor beam to grab it
            I:Component_SetIntLogic_1(7, i, 0, beamTargetIndex)
        else
            I:Log("oh god, forget it")
        end
        --I:Log(tbName)
    end
end
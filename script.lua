while true do
    state = mainmemory.readbyte(0x000E)
    if state == 0x0B then
        savestate.loadslot(1)
    end
    if state == 0x06 then
        savestate.loadslot(1)
    end
    emu.frameadvance()
end
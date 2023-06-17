# DOTA_V

简介：来个热狗🌭

作者：Jeremy.Chim

GitHub：https://github.com/JeremyChim/DOTA_V

## 1、新建文件夹0test

> 路径：…/SteamLibrary/steamapps/common/dota 2 beta/game/dota/0test

## 2、改gameinfo.gi

> 路径：…/SteamLibrary/steamapps/common/dota 2 beta/game/dota/gameinfo.gi

```textile
37        // *LANGUAGE* will be replaced with the actual language name. If not running a specific language, these paths will not be mounted
38        Game                0test
39        Game_Language        dota_*LANGUAGE*
```

## 3、找到pak01_dir.vpk，拉出npc文件

> 路径：…/SteamLibrary/steamapps/common/dota 2 beta/game/dota/pak01_dir.vpk/scripts/ncp

- npc_abilities.txt

- npc_heroes.txt

- npc_units.txt

## 4、下载VPK文件夹

```batch
vpk.exe pak01_dir
move "pak01_dir.vpk" "E:\GamePlatform\Steam\steamapps\common\dota 2 beta\game\0test"
@pause
```

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

## 5、下载MOD
[链接：Dota 2 Skin Mods #8 From Youtube](https://www.youtube.com/watch?v=Wbb0cvLKXqE)  
> 油管[Ant Way大神](https://www.youtube.com/@antway890)的皮肤MOD
> 
[下载：Dota2SkinMod8-v1.zip](https://mega.nz/file/rigWHCKC#nfdgLR9Y4nnLWhYjAfN9OCWaEz4YI3yCaylbWAj9ieo)  
> Mod with Sactum divine terrain & emblem bp 2022  
> 国防部与神圣地形和徽章 bp 2022  

[下载：Dota2SkinMod8-v2.zip](https://mega.nz/file/KqI01IiI#kAAVGlYfsCKUasNKvhYHcu5KBptMvOJ_jM9zW27u4zI)  
> Mod without terrain,ranged effect, & emblem  
> 无地形、远程效果和徽章的Mod  

# GetKnownFolderPath Function

Get system path location as defined by the operating system.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String | Yes |  | String to identify folder to return |

#### Argument 1

String to identify folder to return. The following table lists all the strings currently recognised. Not all of these will return a path on all systems and many are probably not meaningful.

For more information on these values, search the Internet for Microsoft documentation on KNOWNFOLDERID. Information for each will be listed under FOLDERID\_xxx. For example see FOLDERID\_Downloads for information on the folder returned for GetKnownFolderPath('Downloads')

|  |  |  |  |
| --- | --- | --- | --- |
| AdminTools | Pictures | SamplePictures | ConflictFolder |
| CDBurning | PrintHood | SampleVideos | ConnectionsFolder |
| CommonAdminTools | Profile | SavedGames | ControlPanelFolder |
| CommonPrograms | ProgramData | SavedSearches | Games |
| CommonStartMenu | ProgramFiles | SendTo | HomeGroup |
| CommonStartup | ProgramFilesX64 | SidebarDefaultParts | HomeGroupCurrentUser |
| CommonTemplates | ProgramFilesX86 | SidebarParts | InternetFolder |
| Contacts | ProgramFilesCommon | StartMenu | LocalizedResourcesDir |
| Cookies | ProgramFilesCommonX64 | Startup | NetworkFolder |
| Desktop | ProgramFilesCommonX86 | System | OriginalImages |
| DeviceMetadataStore | Programs | SystemX86 | PhotoAlbums |
| Documents | Public | Templates | Playlists |
| DocumentsLibrary | PublicDesktop | UserPinned | PrintersFolder |
| Downloads | PublicDocuments | UserProfiles | PublicUserTiles |
| Favorites | PublicDownloads | UserProgramFiles | RecycleBinFolder |
| Fonts | PublicGameTasks | UserProgramFilesCommon | RoamedTileImages |
| GameTasks | PublicLibraries | Videos | RoamingTiles |
| History | PublicMusic | VideosLibrary | SamplePlaylists |
| ImplicitAppShortcuts | PublicPictures | Windows | Screenshots |
| InternetCache | PublicRingtones |  | SEARCH\_CSC |
| Libraries | PublicVideos | AccountPictures | SearchHome |
| Links | QuickLaunch | AddNewPrograms | SEARCH\_MAPI |
| LocalAppData | Recent | ApplicationShortcuts | SyncManagerFolder |
| LocalAppDataLow | RecordedTVLibrary | AppsFolder | SyncResultsFolder |
| Music | ResourceDir | AppUpdates | SyncSetupFolder |
| MusicLibrary | Ringtones | ChangeRemovePrograms | UsersFiles |
| NetHood | RoamingAppData | CommonOEMLinks | UsersLibraries |
| PicturesLibrary | SampleMusic | ComputerFolder |  |

### Returns

Return type: string

Full path of specified location

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getknownfolderpath) | | |
| [◄ GetKeyDefs](func_getkeydefs.htm) |  | [GetLaplaceErrorMessage ▶](func_getlaplaceerrormessage.htm) |

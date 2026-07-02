# HarmonyOS 应用 API 参考文档目录

## 1. API参考概述

### 1.1. [开发说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/development-intro-api)
### 1.2. [系统能力SystemCapability使用指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/syscap)
### 1.3. [通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)

## 2. 应用框架

### 2.1. Ability Kit（程序框架服务）

#### 2.1.1. ArkTS API

##### 2.1.1.1. Stage模型能力的接口

###### 2.1.1.1.1. [@ohos.app.ability.Ability (Ability基类)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-ability)
###### 2.1.1.1.2. [@ohos.app.ability.AbilityConstant (Ability相关常量)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilityconstant)
###### 2.1.1.1.3. [@ohos.app.ability.abilityLifecycleCallback (UIAbility生命周期回调监听器)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitylifecyclecallback)
###### 2.1.1.1.4. [@ohos.app.ability.AbilityStage (AbilityStage组件管理器)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitystage)
###### 2.1.1.1.5. [@ohos.app.ability.ActionExtensionAbility (支持业务操作自定义的ExtensionAbility组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-actionextensionability)
###### 2.1.1.1.6. [@ohos.app.ability.AgentUIExtensionAbility (带界面的智能体拓展组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-agent-agentuiextensionability)
###### 2.1.1.1.7. [@ohos.app.ability.application (应用工具类)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-application)
###### 2.1.1.1.8. [@ohos.app.ability.ApplicationStateChangeCallback (应用进程状态变化监听器)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-applicationstatechangecallback)
###### 2.1.1.1.9. [@ohos.app.ability.AppServiceExtensionAbility (应用后台服务扩展组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-appserviceextensionability)
###### 2.1.1.1.10. [@ohos.app.ability.AtomicServiceOptions (openAtomicService可选参数)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-atomicserviceoptions)
###### 2.1.1.1.11. [@ohos.app.ability.autoFillManager (自动填充框架)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-autofillmanager)
###### 2.1.1.1.12. [@ohos.app.ability.ChildProcess (子进程基类)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-childprocess)
###### 2.1.1.1.13. [@ohos.app.ability.childProcessManager (子进程管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-childprocessmanager)
###### 2.1.1.1.14. [@ohos.app.ability.ChildProcessArgs (子进程参数)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-childprocessargs)
###### 2.1.1.1.15. [@ohos.app.ability.ChildProcessOptions (子进程启动选项)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-childprocessoptions)
###### 2.1.1.1.16. [@ohos.app.ability.common (Ability公共模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-common)
###### 2.1.1.1.17. [@ohos.app.ability.CompletionHandler (拉起应用结果的操作类)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-completionhandler)
###### 2.1.1.1.18. [@ohos.app.ability.CompletionHandlerForAtomicService (打开元服务结果的操作类)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-completionhandlerforatomicservice)
###### 2.1.1.1.19. [@ohos.app.ability.CompletionHandlerForAbilityStartCallback (拉起应用结果回调的操作类)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-completionhandlerforabilitystartcallback)
###### 2.1.1.1.20. [@ohos.app.ability.contextConstant (Context相关常量)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-contextconstant)
###### 2.1.1.1.21. [@ohos.app.ability.EmbeddableUIAbility (可嵌入式UIAbility组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-embeddableuiability)
###### 2.1.1.1.22. [@ohos.app.ability.EmbeddedUIExtensionAbility (支持跨进程界面嵌入的ExtensionAbility组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-embeddeduiextensionability)
###### 2.1.1.1.23. [@ohos.app.ability.EnvironmentCallback (系统环境变化监听器)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-environmentcallback)
###### 2.1.1.1.24. [@ohos.app.ability.ExtensionAbility (扩展能力基类)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-extensionability)
###### 2.1.1.1.25. [@ohos.app.ability.insightIntent (意图框架基础定义)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-insightintent)
###### 2.1.1.1.26. [@ohos.app.ability.InsightIntentContext (意图执行上下文)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-insightintentcontext)
###### 2.1.1.1.27. [@ohos.app.ability.InsightIntentDecorator (意图装饰器定义)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-insightintentdecorator)
###### 2.1.1.1.28. [@ohos.app.ability.InsightIntentEntryExecutor (@InsightIntentEntry的意图执行基类)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-insightintententryexecutor)
###### 2.1.1.1.29. [@ohos.app.ability.InsightIntentExecutor (意图执行基类)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-insightintentexecutor)
###### 2.1.1.1.30. [@ohos.app.ability.insightIntentProvider (意图提供方管理能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-insightintentprovider)
###### 2.1.1.1.31. [@ohos.app.ability.PhotoEditorExtensionAbility (支持图片编辑能力的ExtensionAbility组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-photoeditorextensionability)
###### 2.1.1.1.32. [@ohos.app.ability.OpenLinkOptions (openLink的可选参数)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-openlinkoptions)
###### 2.1.1.1.33. [@ohos.app.ability.ShareExtensionAbility (支持分享详情页接入的ExtensionAbility组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-shareextensionability)
###### 2.1.1.1.34. [@ohos.app.ability.StartOptions (startAbility的可选参数)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-startoptions)
###### 2.1.1.1.35. [@ohos.app.ability.systemConfiguration (系统环境模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-systemconfiguration)
###### 2.1.1.1.36. [@ohos.app.ability.UIAbility (带界面的应用组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)
###### 2.1.1.1.37. [@ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensionability)
###### 2.1.1.1.38. [@ohos.app.ability.UIExtensionContentSession (带界面扩展能力的界面操作类)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensioncontentsession)
###### 2.1.1.1.39. [@ohos.app.ability.sendableContextManager (sendable上下文管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-sendablecontextmanager)
###### 2.1.1.1.40. [@ohos.app.ability.scriptManager (脚本管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-scriptmanager)
###### 2.1.1.1.41. [@ohos.app.appstartup.StartupConfig (启动框架配置信息)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startupconfig)
###### 2.1.1.1.42. [@ohos.app.appstartup.StartupConfigEntry (启动框架配置)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startupconfigentry)
###### 2.1.1.1.43. [@ohos.app.appstartup.StartupListener (启动框架任务监听器)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startuplistener)
###### 2.1.1.1.44. [@ohos.app.appstartup.startupManager (启动框架管理能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startupmanager)
###### 2.1.1.1.45. [@ohos.app.appstartup.StartupTask (启动框架任务)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startuptask)
###### 2.1.1.1.46. [@ohos.app.ability.autoStartupManager (开机自启管理能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-autostartupmanager)
###### 2.1.1.1.47. [@ohos.app.agent.agentConstant (Agent常量)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-agent-agentconstant)
###### 2.1.1.1.48. [@ohos.app.agent.AgentExtensionAbility (智能体扩展组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-agent-agentextensionability)
###### 2.1.1.1.49. [@ohos.continuation.continuationManager (流转/协同管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationmanager)
###### 2.1.1.1.50. continuation

###### 2.1.1.1.50.1. [ContinuationExtraParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationextraparams)
###### 2.1.1.1.50.2. [ContinuationResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationresult)
##### 2.1.1.2. FA模型能力的接口

###### 2.1.1.2.1. [@ohos.ability.ability (Ability模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-ability)
###### 2.1.1.2.2. [@ohos.ability.featureAbility (FeatureAbility模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-featureability)
###### 2.1.1.2.3. [@ohos.ability.particleAbility (ParticleAbility模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-particleability)
###### 2.1.1.2.4. ability

###### 2.1.1.2.4.1. [DataAbilityOperation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-dataabilityoperation)
###### 2.1.1.2.4.2. [DataAbilityResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-dataabilityresult)
###### 2.1.1.2.4.3. [StartAbilityParameter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-startabilityparameter)
###### 2.1.1.2.5. app

###### 2.1.1.2.5.1. [AppVersionInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-appversioninfo)
###### 2.1.1.2.5.2. [Context (FA模型的上下文基类)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-context)
###### 2.1.1.2.5.3. [ProcessInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-processinfo)
##### 2.1.1.3. 通用能力的接口(推荐)

###### 2.1.1.3.1. [@ohos.abilityAccessCtrl (程序访问控制管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-abilityaccessctrl)
###### 2.1.1.3.2. [@ohos.ability.screenLockFileManager (锁屏敏感数据管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-screenlockfilemanager)
###### 2.1.1.3.3. [@ohos.app.ability.abilityManager (Ability信息管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitymanager)
###### 2.1.1.3.4. [@ohos.app.ability.appManager (应用管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-appmanager)
###### 2.1.1.3.5. [@ohos.app.ability.appRecovery (应用故障恢复)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-apprecovery)
###### 2.1.1.3.6. [@ohos.app.ability.Configuration (环境变量)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-configuration)
###### 2.1.1.3.7. [@ohos.app.ability.ConfigurationConstant (环境变量相关的常量定义)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-configurationconstant)
###### 2.1.1.3.8. [@ohos.app.ability.continueManager (跨端迁移)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-continuemanager)
###### 2.1.1.3.9. [@ohos.app.ability.dataUriUtils (DataUriUtils模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-datauriutils)
###### 2.1.1.3.10. [@ohos.app.ability.dialogRequest (dialogRequest模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-dialogrequest)
###### 2.1.1.3.11. [@ohos.app.ability.errorManager (错误管理模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-errormanager)
###### 2.1.1.3.12. [@ohos.app.ability.hyperSnapManager (应用快启管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-hypersnapmanager)
###### 2.1.1.3.13. [@ohos.app.ability.kioskManager (Kiosk模式管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-kioskmanager)
###### 2.1.1.3.14. [@ohos.app.ability.Want (Want)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want)
###### 2.1.1.3.15. [@ohos.app.ability.wantAgent (WantAgent模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-wantagent)
###### 2.1.1.3.16. [@ohos.app.ability.wantConstant (Want常量)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-wantconstant)
###### 2.1.1.3.17. [@ohos.bundle.bundleManager (应用程序包管理模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager)
###### 2.1.1.3.18. [@ohos.bundle.defaultAppManager (默认应用管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-defaultappmanager)
###### 2.1.1.3.19. [@ohos.bundle.launcherBundleManager (launcherBundleManager模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-launcherbundlemanager)
###### 2.1.1.3.20. [@ohos.bundle.overlay (overlay特征模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-overlay)
###### 2.1.1.3.21. [@ohos.bundle.shortcutManager (shortcutManager模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-shortcutmanager)
###### 2.1.1.3.22. [@ohos.bundle.skillManager (skillManager模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-skillmanager)
##### 2.1.1.4. 接口依赖的元素及定义

###### 2.1.1.4.1. ability

###### 2.1.1.4.1.1. [AbilityResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-abilityresult)
###### 2.1.1.4.1.2. [ConnectOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-connectoptions)
###### 2.1.1.4.1.3. [DataAbilityHelper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-dataabilityhelper)
###### 2.1.1.4.2. application

###### 2.1.1.4.2.1. [AbilityMonitor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitymonitor)
###### 2.1.1.4.2.2. [AbilityRunningInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilityrunninginfo)
###### 2.1.1.4.2.3. [AbilityStageContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitystagecontext)
###### 2.1.1.4.2.4. [AbilityStageMonitor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitystagemonitor)
###### 2.1.1.4.2.5. [AbilityStartCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitystartcallback)
###### 2.1.1.4.2.6. [AbilityStateData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitystatedata)
###### 2.1.1.4.2.7. [AgentCard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-agentcard)
###### 2.1.1.4.2.8. [AgentExtensionContext (智能体扩展组件上下文)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-agentextensioncontext)
###### 2.1.1.4.2.9. [AgentHostProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-agenthostproxy)
###### 2.1.1.4.2.10. [ApplicationContext (应用上下文)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationcontext)
###### 2.1.1.4.2.11. [ApplicationStateObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationstateobserver)
###### 2.1.1.4.2.12. [AppServiceExtensionContext (应用后台服务扩展组件上下文)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-appserviceextensioncontext)
###### 2.1.1.4.2.13. [AppStateData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-appstatedata)
###### 2.1.1.4.2.14. [BaseContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-basecontext)
###### 2.1.1.4.2.15. [Context (Stage模型的上下文基类)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)
###### 2.1.1.4.2.16. [EmbeddableUIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-embeddableuiabilitycontext)
###### 2.1.1.4.2.17. [ErrorObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-errorobserver)
###### 2.1.1.4.2.18. [EventHub](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-eventhub)
###### 2.1.1.4.2.19. [ExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-extensioncontext)
###### 2.1.1.4.2.20. [KioskStatus (Kiosk状态信息)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-kioskstatus)
###### 2.1.1.4.2.21. [LoopObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-loopobserver)
###### 2.1.1.4.2.22. [ProcessInformation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-processinformation)
###### 2.1.1.4.2.23. [ProcessRunningInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-processrunninginfo)
###### 2.1.1.4.2.24. [UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)
###### 2.1.1.4.2.25. [UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext)
###### 2.1.1.4.2.26. [UIServiceExtensionConnectCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiserviceextensionconnectcallback)
###### 2.1.1.4.2.27. [UIServiceProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiserviceproxy)
###### 2.1.1.4.2.28. [ProcessData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-processdata)
###### 2.1.1.4.2.29. [PhotoEditorExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-photoeditorextensioncontext)
###### 2.1.1.4.2.30. [SendableContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-sendablecontext)
###### 2.1.1.4.3. bundleManager

###### 2.1.1.4.3.1. [AbilityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-abilityinfo)
###### 2.1.1.4.3.2. [ApplicationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-applicationinfo)
###### 2.1.1.4.3.3. [BundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-bundleinfo)
###### 2.1.1.4.3.4. [ElementName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-elementname)
###### 2.1.1.4.3.5. [ExtensionAbilityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-extensionabilityinfo)
###### 2.1.1.4.3.6. [HapModuleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-hapmoduleinfo)
###### 2.1.1.4.3.7. [LauncherAbilityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-launcherabilityinfo)
###### 2.1.1.4.3.8. [Metadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-metadata)
###### 2.1.1.4.3.9. [OverlayModuleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-overlaymoduleinfo)
###### 2.1.1.4.3.10. [Skill](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-skill)
###### 2.1.1.4.3.11. [ShortcutInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-shortcutinfo)
###### 2.1.1.4.3.12. [SkillInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-skillinfo)
###### 2.1.1.4.4. security

###### 2.1.1.4.4.1. [PermissionRequestResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-permissionrequestresult)
###### 2.1.1.4.5. wantAgent

###### 2.1.1.4.5.1. [TriggerInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-wantagent-triggerinfo)
###### 2.1.1.4.5.2. [WantAgentInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-wantagent-wantagentinfo)
##### 2.1.1.5. 已停止维护的接口

###### 2.1.1.5.1. [@ohos.ability.dataUriUtils (DataUriUtils模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-datauriutils)
###### 2.1.1.5.2. [@ohos.ability.errorCode (ErrorCode)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-errorcode)
###### 2.1.1.5.3. [@ohos.ability.wantConstant (wantConstant)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-wantconstant)
###### 2.1.1.5.4. [@ohos.application.appManager (appManager)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-appmanager)
###### 2.1.1.5.5. [@ohos.application.Configuration (Configuration)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-configuration)
###### 2.1.1.5.6. [@ohos.application.ConfigurationConstant (ConfigurationConstant)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-configurationconstant)
###### 2.1.1.5.7. [@ohos.application.Want (Want)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-want)
###### 2.1.1.5.8. [@ohos.wantAgent (WantAgent模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wantagent)
###### 2.1.1.5.9. [@ohos.bundle (Bundle模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle)
###### 2.1.1.5.10. [@system.package (应用管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-package)
###### 2.1.1.5.11. ability

###### 2.1.1.5.11.1. [Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-want)
###### 2.1.1.5.12. bundle

###### 2.1.1.5.12.1. [AbilityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-abilityinfo)
###### 2.1.1.5.12.2. [ApplicationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-applicationinfo)
###### 2.1.1.5.12.3. [BundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-bundleinfo)
###### 2.1.1.5.12.4. [CustomizeData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-customizedata)
###### 2.1.1.5.12.5. [ElementName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-elementname)
###### 2.1.1.5.12.6. [HapModuleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-hapmoduleinfo)
###### 2.1.1.5.12.7. [ModuleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-moduleinfo)
###### 2.1.1.5.12.8. [ShortcutInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-shortcutinfo)
#### 2.1.2. C API

##### 2.1.2.1. 模块

###### 2.1.2.1.1. [AbilityAccessControl](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityaccesscontrol)
###### 2.1.2.1.2. [AbilityBase](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilitybase)
###### 2.1.2.1.3. [AbilityRuntime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime)
###### 2.1.2.1.4. [Native_Bundle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle)
###### 2.1.2.1.5. [ChildProcess](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-childprocess)
##### 2.1.2.2. 头文件

###### 2.1.2.2.1. [ability_access_control.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-access-control-h)
###### 2.1.2.2.2. [ability_base_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-base-common-h)
###### 2.1.2.2.3. [ability_runtime_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h)
###### 2.1.2.2.4. [application_context.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-application-context-h)
###### 2.1.2.2.5. [context_constant.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-context-constant-h)
###### 2.1.2.2.6. [native_child_process.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-child-process-h)
###### 2.1.2.2.7. [native_interface_bundle.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-bundle-h)
###### 2.1.2.2.8. [start_options.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-start-options-h)
###### 2.1.2.2.9. [want.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-want-h)
###### 2.1.2.2.10. [ability_resource_info.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-resource-info-h)
###### 2.1.2.2.11. [bundle_manager_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-bundle-manager-common-h)
###### 2.1.2.2.12. [context.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-context-h)
###### 2.1.2.2.13. [extension_ability.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-extension-ability-h)
###### 2.1.2.2.14. [modular_object_extension_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-modular-object-extension-manager-h)
##### 2.1.2.3. 结构体

###### 2.1.2.3.1. [AbilityBase_Element](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilitybase-element)
###### 2.1.2.3.2. [AbilityBase_Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilitybase-want)
###### 2.1.2.3.3. [AbilityRuntime_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions)
###### 2.1.2.3.4. [NativeChildProcess_Fd](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativechildprocess-fd)
###### 2.1.2.3.5. [NativeChildProcess_FdList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativechildprocess-fdlist)
###### 2.1.2.3.6. [NativeChildProcess_Options](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativechildprocess-options)
###### 2.1.2.3.7. [NativeChildProcess_Args](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativechildprocess-args)
###### 2.1.2.3.8. [Ability_ChildProcessConfigs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-childprocessconfigs)
###### 2.1.2.3.9. [OH_NativeBundle_ApplicationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle-oh-nativebundle-applicationinfo)
###### 2.1.2.3.10. [OH_NativeBundle_ElementName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle-oh-nativebundle-elementname)
###### 2.1.2.3.11. [OH_NativeBundle_Metadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle-oh-nativebundle-metadata)
###### 2.1.2.3.12. [OH_NativeBundle_ModuleMetadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle-oh-nativebundle-modulemetadata)
###### 2.1.2.3.13. [OH_NativeBundle_AbilityResourceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle-oh-nativebundle-abilityresourceinfo)
###### 2.1.2.3.14. [AbilityRuntime_Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-abilityruntime-context)
###### 2.1.2.3.15. [AbilityRuntime_Context*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-abilityruntime-context8h)
###### 2.1.2.3.16. [AbilityRuntime_ExtensionInstance](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-extensioninstance)
###### 2.1.2.3.17. [AbilityRuntime_ExtensionInstance*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-extensioninstance8h)
###### 2.1.2.3.18. [OH_AbilityRuntime_ModularObjectExtensionInfo*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-oh-abilityruntime-modularobjectextensioninfo8h)
###### 2.1.2.3.19. [OH_AbilityRuntime_AllModularObjectExtensionInfos*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-oh-abilityruntime-allmodularobjectextensioninfos8h)
#### 2.1.3. 错误码

##### 2.1.3.1. [元能力子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-ability)
##### 2.1.3.2. [DistributedSchedule错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-distributedschedule)
##### 2.1.3.3. [包管理子系统通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bundle)
##### 2.1.3.4. [访问控制错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-access-token)
##### 2.1.3.5. [锁屏敏感数据管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-screenlockfilemanager)
### 2.2. Accessibility Kit（无障碍服务）

#### 2.2.1. ArkTS API

##### 2.2.1.1. [@ohos.accessibility (辅助功能)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-accessibility)
##### 2.2.1.2. [@ohos.accessibility.GesturePath (手势路径)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-accessibility-gesturepath)
##### 2.2.1.3. [@ohos.accessibility.GesturePoint (手势触摸点)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-accessibility-gesturepoint)
##### 2.2.1.4. [@ohos.application.AccessibilityExtensionAbility (辅助功能扩展能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-accessibilityextensionability)
##### 2.2.1.5. [AccessibilityExtensionContext (辅助功能扩展上下文)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-accessibilityextensioncontext)
#### 2.2.2. 错误码

##### 2.2.2.1. [无障碍子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-accessibility)
### 2.3. ArkData（方舟数据管理）

#### 2.3.1. ArkTS API

##### 2.3.1.1. [@ohos.data.commonType (数据通用类型)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-commontype)
##### 2.3.1.2. [@ohos.data.dataAbility（DataAbility谓词）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-ability)
##### 2.3.1.3. [@ohos.data.dataShare (数据共享)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-datashare)
##### 2.3.1.4. [@ohos.data.dataSharePredicates (数据共享谓词)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-datasharepredicates)
##### 2.3.1.5. [@ohos.data.distributedDataObject (分布式数据对象)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-distributedobject)
##### 2.3.1.6. [@ohos.data.distributedKVStore (分布式键值数据库)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributedkvstore)
##### 2.3.1.7. [@ohos.data.preferences (用户首选项)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-preferences)
##### 2.3.1.8. [@ohos.data.sendablePreferences (共享用户首选项)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-sendablepreferences)
##### 2.3.1.9. @ohos.data.relationalStore (关系型数据库)

###### 2.3.1.9.1. [模块描述](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore)
###### 2.3.1.9.2. [Functions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-f)
###### 2.3.1.9.3. [Interface (RdbStore)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-rdbstore)
###### 2.3.1.9.4. [Interface (ResultSet)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-resultset)
###### 2.3.1.9.5. [Class (LiteResultSet)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-literesultset)
###### 2.3.1.9.6. [Interface (Transaction)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-transaction)
###### 2.3.1.9.7. [Interfaces (其他)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-i)
###### 2.3.1.9.8. [Class (RdbPredicates)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-rdbpredicates)
###### 2.3.1.9.9. [Enums](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-e)
###### 2.3.1.9.10. [Types](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-t)
##### 2.3.1.10. [@ohos.data.sendableRelationalStore（共享关系型数据库）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-sendablerelationalstore)
##### 2.3.1.11. [@ohos.data.unifiedDataChannel (标准化数据通路)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-unifieddatachannel)
##### 2.3.1.12. [@ohos.data.uniformDataStruct (标准化数据结构)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-uniformdatastruct)
##### 2.3.1.13. [@ohos.data.uniformTypeDescriptor (标准化数据定义与描述)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-uniformtypedescriptor)
##### 2.3.1.14. [@ohos.data.ValuesBucket (数据集)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-valuesbucket)
##### 2.3.1.15. [@ohos.data.intelligence (智慧数据平台)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-intelligence)
##### 2.3.1.16. [@ohos.data.cloudData (端云服务)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-clouddata)
##### 2.3.1.17. 已停止维护的接口

###### 2.3.1.17.1. [@ohos.data.distributedData (分布式数据管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributed-data)
###### 2.3.1.17.2. [@ohos.data.rdb（关系型数据库）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-rdb)
###### 2.3.1.17.3. [@ohos.data.storage (轻量级存储)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-storage)
###### 2.3.1.17.4. [@system.storage (数据存储)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-storage)
###### 2.3.1.17.5. data/rdb

###### 2.3.1.17.5.1. [resultSet（结果集）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-resultset)
#### 2.3.2. ArkTS 组件

##### 2.3.2.1. [@ohos.data.UdmfComponents (内容卡片)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-udmfcomponents)
#### 2.3.3. C API

##### 2.3.3.1. 模块

###### 2.3.3.1.1. [Preferences](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-preferences)
###### 2.3.3.1.2. [RDB](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb)
###### 2.3.3.1.3. [UDMF](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf)
##### 2.3.3.2. 头文件

###### 2.3.3.2.1. [oh_preferences.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-preferences-h)
###### 2.3.3.2.2. [oh_preferences_err_code.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-preferences-err-code-h)
###### 2.3.3.2.3. [oh_preferences_option.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-preferences-option-h)
###### 2.3.3.2.4. [oh_preferences_value.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-preferences-value-h)
###### 2.3.3.2.5. [data_asset.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-data-asset-h)
###### 2.3.3.2.6. [oh_cursor.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-cursor-h)
###### 2.3.3.2.7. [oh_data_value.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-data-value-h)
###### 2.3.3.2.8. [oh_data_values.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-data-values-h)
###### 2.3.3.2.9. [oh_data_values_buckets.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-data-values-buckets-h)
###### 2.3.3.2.10. [oh_predicates.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-predicates-h)
###### 2.3.3.2.11. [oh_rdb_crypto_param.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-rdb-crypto-param-h)
###### 2.3.3.2.12. [oh_rdb_transaction.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-rdb-transaction-h)
###### 2.3.3.2.13. [oh_rdb_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-rdb-types-h)
###### 2.3.3.2.14. [oh_value_object.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-value-object-h)
###### 2.3.3.2.15. [oh_values_bucket.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-values-bucket-h)
###### 2.3.3.2.16. [relational_store.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-relational-store-h)
###### 2.3.3.2.17. [relational_store_error_code.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-relational-store-error-code-h)
###### 2.3.3.2.18. [udmf.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-h)
###### 2.3.3.2.19. [udmf_err_code.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-err-code-h)
###### 2.3.3.2.20. [udmf_meta.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-meta-h)
###### 2.3.3.2.21. [uds.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-uds-h)
###### 2.3.3.2.22. [utd.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-utd-h)
##### 2.3.3.3. 结构体

###### 2.3.3.3.1. [OH_Cursor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-cursor)
###### 2.3.3.3.2. [OH_Predicates](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-predicates)
###### 2.3.3.3.3. [OH_RDB_ReturningContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-returningcontext)
###### 2.3.3.3.4. [OH_VObject](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-vobject)
###### 2.3.3.3.5. [OH_VBucket](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-vbucket)
###### 2.3.3.3.6. [OH_Rdb_Config](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-config)
###### 2.3.3.3.7. [OH_Rdb_Store](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-store)
###### 2.3.3.3.8. [Rdb_DistributedConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-distributedconfig)
###### 2.3.3.3.9. [Rdb_KeyInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-keyinfo)
###### 2.3.3.3.10. [Rdb_KeyData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-keydata)
###### 2.3.3.3.11. [Rdb_ChangeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-changeinfo)
###### 2.3.3.3.12. [Rdb_SubscribeCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-subscribecallback)
###### 2.3.3.3.13. [Rdb_DataObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-dataobserver)
###### 2.3.3.3.14. [Rdb_Statistic](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-statistic)
###### 2.3.3.3.15. [Rdb_TableDetails](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-tabledetails)
###### 2.3.3.3.16. [Rdb_ProgressDetails](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-progressdetails)
###### 2.3.3.3.17. [Rdb_ProgressObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-progressobserver)
###### 2.3.3.3.18. [OH_Preferences](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-preferences-oh-preferences)
###### 2.3.3.3.19. [OH_PreferencesOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-preferences-oh-preferencesoption)
###### 2.3.3.3.20. [OH_PreferencesPair](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-preferences-oh-preferencespair)
###### 2.3.3.3.21. [OH_PreferencesValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-preferences-oh-preferencesvalue)
###### 2.3.3.3.22. [Data_Asset](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-data-asset)
###### 2.3.3.3.23. [OH_Data_Value](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-data-value)
###### 2.3.3.3.24. [OH_Data_Values](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-data-values)
###### 2.3.3.3.25. [OH_Data_VBuckets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-data-vbuckets)
###### 2.3.3.3.26. [OH_Rdb_CryptoParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-cryptoparam)
###### 2.3.3.3.27. [OH_RDB_TransOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-transoptions)
###### 2.3.3.3.28. [OH_Rdb_Transaction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-transaction)
###### 2.3.3.3.29. [OH_Rdb_ConfigV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-configv2)
###### 2.3.3.3.30. [OH_UdmfData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-oh-udmfdata)
###### 2.3.3.3.31. [OH_UdmfRecord](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-oh-udmfrecord)
###### 2.3.3.3.32. [OH_UdmfRecordProvider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-oh-udmfrecordprovider)
###### 2.3.3.3.33. [OH_UdmfProperty](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-oh-udmfproperty)
###### 2.3.3.3.34. [OH_Udmf_ProgressInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-oh-udmf-progressinfo)
###### 2.3.3.3.35. [OH_UdmfGetDataParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-oh-udmfgetdataparams)
###### 2.3.3.3.36. [OH_UdmfOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-oh-udmfoptions)
###### 2.3.3.3.37. [OH_UdmfDataLoadParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-oh-udmfdataloadparams)
###### 2.3.3.3.38. [OH_UdmfDataLoadInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-oh-udmfdataloadinfo)
###### 2.3.3.3.39. [OH_UdsPlainText](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-oh-udsplaintext)
###### 2.3.3.3.40. [OH_UdsHyperlink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-oh-udshyperlink)
###### 2.3.3.3.41. [OH_UdsHtml](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-oh-udshtml)
###### 2.3.3.3.42. [OH_UdsAppItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-oh-udsappitem)
###### 2.3.3.3.43. [OH_UdsFileUri](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-oh-udsfileuri)
###### 2.3.3.3.44. [OH_UdsPixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-oh-udspixelmap)
###### 2.3.3.3.45. [OH_UdsArrayBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-oh-udsarraybuffer)
###### 2.3.3.3.46. [OH_UdsContentForm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-oh-udscontentform)
###### 2.3.3.3.47. [OH_UdsDetails](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-oh-udsdetails)
###### 2.3.3.3.48. [OH_Utd](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-oh-utd)
#### 2.3.4. 错误码

##### 2.3.4.1. [关系型数据库错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-data-rdb)
##### 2.3.4.2. [数据共享错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-datashare)
##### 2.3.4.3. [分布式数据对象错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-distributed-dataobject)
##### 2.3.4.4. [分布式键值数据库错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-distributedkvstore)
##### 2.3.4.5. [用户首选项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences)
##### 2.3.4.6. [统一数据管理框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-udmf)
##### 2.3.4.7. [智慧数据平台错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-intelligence)
### 2.4. ArkTS（方舟编程语言）

#### 2.4.1. ArkTS API

##### 2.4.1.1. @arkts.collections (ArkTS容器集)

###### 2.4.1.1.1. [模块描述](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections)
###### 2.4.1.1.2. [Class (Array)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-array)
###### 2.4.1.1.3. [Class (Map)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-map)
###### 2.4.1.1.4. [Class (Set)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-set)
###### 2.4.1.1.5. [Class (ArrayBuffer)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-arraybuffer)
###### 2.4.1.1.6. [Class (Int8Array)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-int8array)
###### 2.4.1.1.7. [Class (Uint8Array)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-uint8array)
###### 2.4.1.1.8. [Class (Int16Array)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-int16array)
###### 2.4.1.1.9. [Class (Uint16Array)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-uint16array)
###### 2.4.1.1.10. [Class (Int32Array)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-int32array)
###### 2.4.1.1.11. [Class (Uint32Array)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-uint32array)
###### 2.4.1.1.12. [Class (Uint8ClampedArray)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-uint8clampedarray)
###### 2.4.1.1.13. [Class (Float32Array)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-float32array)
###### 2.4.1.1.14. [Class (BitVector)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-bitvector)
###### 2.4.1.1.15. [Interface (ConcatArray)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-concatarray)
###### 2.4.1.1.16. [Types](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-types)
##### 2.4.1.2. [@arkts.lang (ArkTS语言基础能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkts-lang)
##### 2.4.1.3. [@arkts.math.Decimal (高精度数学库Decimal)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkts-decimal)
##### 2.4.1.4. @arkts.utils (ArkTS工具库)

###### 2.4.1.4.1. [模块描述](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-utils)
###### 2.4.1.4.2. [Functions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-utils-f)
###### 2.4.1.4.3. [ArkTSUtils.locks](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-utils-locks)
###### 2.4.1.4.4. [ArkTSUtils.ASON](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-utils-ason)
###### 2.4.1.4.5. [SendableLruCache<K, V>](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-utils-sendablelrucache)
##### 2.4.1.5. [@ohos.buffer (Buffer)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-buffer)
##### 2.4.1.6. [@ohos.convertxml (xml转换JavaScript)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-convertxml)
##### 2.4.1.7. [@ohos.fastbuffer (FastBuffer)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-fastbuffer)
##### 2.4.1.8. [@ohos.process (获取进程相关的信息)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-process)
##### 2.4.1.9. [@ohos.taskpool (启动任务池)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-taskpool)
##### 2.4.1.10. [@ohos.uri (URI字符串解析)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uri)
##### 2.4.1.11. [@ohos.url (URL字符串解析)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-url)
##### 2.4.1.12. [@ohos.util (util工具函数)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util)
##### 2.4.1.13. [@ohos.util.ArrayList (线性容器ArrayList)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arraylist)
##### 2.4.1.14. [@ohos.util.Deque (线性容器Deque)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-deque)
##### 2.4.1.15. [@ohos.util.HashMap (非线性容器HashMap)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hashmap)
##### 2.4.1.16. [@ohos.util.HashSet (非线性容器HashSet)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hashset)
##### 2.4.1.17. [@ohos.util.json (JSON解析与生成)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-json)
##### 2.4.1.18. [@ohos.util.LightWeightMap (非线性容器LightWeightMap)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-lightweightmap)
##### 2.4.1.19. [@ohos.util.LightWeightSet (非线性容器LightWeightSet)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-lightweightset)
##### 2.4.1.20. [@ohos.util.LinkedList (线性容器LinkedList)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-linkedlist)
##### 2.4.1.21. [@ohos.util.List (线性容器List)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-list)
##### 2.4.1.22. [@ohos.util.PlainArray (非线性容器PlainArray)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-plainarray)
##### 2.4.1.23. [@ohos.util.Queue (线性容器Queue)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-queue)
##### 2.4.1.24. [@ohos.util.Stack (线性容器Stack)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-stack)
##### 2.4.1.25. [@ohos.util.stream (数据流基类stream)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-stream)
##### 2.4.1.26. [@ohos.util.TreeMap (非线性容器TreeMap)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-treemap)
##### 2.4.1.27. [@ohos.util.TreeSet (非线性容器TreeSet)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-treeset)
##### 2.4.1.28. [@ohos.worker (启动一个Worker)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-worker)
##### 2.4.1.29. [@ohos.xml (XML解析与生成)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-xml)
##### 2.4.1.30. 已停止维护的接口

###### 2.4.1.30.1. [@ohos.util.Vector (线性容器Vector)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-vector)
#### 2.4.2. 错误码

##### 2.4.2.1. [语言基础类库错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-utils)
##### 2.4.2.2. [TypeScript Compiler错误码介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-tsc)
##### 2.4.2.3. [编译工具链错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-ets-loader)
##### 2.4.2.4. [es2abc编译器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-es2abc)
##### 2.4.2.5. [源码混淆错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-source-obfuscation)
### 2.5. ArkUI（方舟UI框架）

#### 2.5.1. ArkTS API

##### 2.5.1.1. UI界面

###### 2.5.1.1.1. [@ohos.animator (动画)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-animator)
###### 2.5.1.1.2. [@ohos.arkui.componentSnapshot (组件截图)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-componentsnapshot)
###### 2.5.1.1.3. [@ohos.arkui.componentUtils (componentUtils)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-componentutils)
###### 2.5.1.1.4. [@ohos.arkui.dragController (DragController)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-dragcontroller)
###### 2.5.1.1.5. [@ohos.arkui.drawableDescriptor (DrawableDescriptor)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor)
###### 2.5.1.1.6. [@ohos.arkui.inspector (布局回调)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-inspector)
###### 2.5.1.1.7. [@ohos.arkui.node (自定义节点)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-node)
###### 2.5.1.1.8. [@ohos.arkui.observer (无感监听)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-observer)
###### 2.5.1.1.9. [@ohos.arkui.Prefetcher (Prefetching)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-prefetcher)
###### 2.5.1.1.10. [@ohos.arkui.shape (形状)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-shape)
###### 2.5.1.1.11. [@ohos.arkui.theme(主题换肤)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-theme)
###### 2.5.1.1.12. @ohos.arkui.UIContext (UIContext)

###### 2.5.1.1.12.1. [模块描述](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext)
###### 2.5.1.1.12.2. [Class (ComponentSnapshot)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-componentsnapshot)
###### 2.5.1.1.12.3. [Class (ComponentUtils)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-componentutils)
###### 2.5.1.1.12.4. [Class (ContextMenuController)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-contextmenucontroller)
###### 2.5.1.1.12.5. [Class (CursorController)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-cursorcontroller)
###### 2.5.1.1.12.6. [Class (DragController)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-dragcontroller)
###### 2.5.1.1.12.7. [Class (DynamicSyncScene)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-dynamicsyncscene)
###### 2.5.1.1.12.8. [Class (FocusController)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-focuscontroller)
###### 2.5.1.1.12.9. [Class (Font)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-font)
###### 2.5.1.1.12.10. [Class (FrameCallback)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-framecallback)
###### 2.5.1.1.12.11. [Class (Magnifier)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-magnifier)
###### 2.5.1.1.12.12. [Class (MarqueeDynamicSyncScene)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-marqueedynamicsyncscene)
###### 2.5.1.1.12.13. [Class (MeasureUtils)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-measureutils)
###### 2.5.1.1.12.14. [Class (MediaQuery)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-mediaquery)
###### 2.5.1.1.12.15. [Class (OverlayManager)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-overlaymanager)
###### 2.5.1.1.12.16. [Class (PromptAction)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction)
###### 2.5.1.1.12.17. [Class (Router)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)
###### 2.5.1.1.12.18. [Class (SwiperDynamicSyncScene)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-swiperdynamicsyncscene)
###### 2.5.1.1.12.19. [Class (TextMenuController)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller)
###### 2.5.1.1.12.20. [Class (UIContext)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)
###### 2.5.1.1.12.21. [Class (ResolvedUIContext)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-resolveduicontext)
###### 2.5.1.1.12.22. [Class (UIInspector)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uiinspector)
###### 2.5.1.1.12.23. [Class (UIObserver)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uiobserver)
###### 2.5.1.1.12.24. [Interface (AtomicServiceBar)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-atomicservicebar)
###### 2.5.1.1.12.25. [Interfaces (其他)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-i)
###### 2.5.1.1.12.26. [Enums](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-e)
###### 2.5.1.1.12.27. [Types](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-t)
###### 2.5.1.1.13. [@ohos.arkui.uiExtension (uiExtension)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-uiextension)
###### 2.5.1.1.14. [@ohos.arkui.uiMaterial (系统材质)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uimaterial)
###### 2.5.1.1.15. [@ohos.arkui.StateManagement (状态管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-statemanagement)
###### 2.5.1.1.16. [@ohos.curves (插值计算)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-curve)
###### 2.5.1.1.17. [@ohos.font (注册自定义字体)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-font)
###### 2.5.1.1.18. [@ohos.matrix4 (矩阵变换)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-matrix4)
###### 2.5.1.1.19. [@ohos.measure (文本计算)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-measure)
###### 2.5.1.1.20. [@ohos.mediaquery (媒体查询)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-mediaquery)
###### 2.5.1.1.21. [@ohos.pluginComponent (PluginComponentManager)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-plugincomponent)
###### 2.5.1.1.22. [@ohos.promptAction (弹窗)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-promptaction)
###### 2.5.1.1.23. [@ohos.router (页面路由)(不推荐)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-router)
###### 2.5.1.1.24. [@ohos.uiAppearance (用户界面外观)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uiappearance)
###### 2.5.1.1.25. [getContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-getcontext)
###### 2.5.1.1.26. [postCardAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-postcardaction)
###### 2.5.1.1.27. arkui

###### 2.5.1.1.27.1. [BuilderNode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-buildernode)
###### 2.5.1.1.27.2. [ComponentContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-componentcontent)
###### 2.5.1.1.27.3. [FrameNode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-framenode)
###### 2.5.1.1.27.4. [Graphics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics)
###### 2.5.1.1.27.5. [LayoutAlgorithm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-layoutalgorithm)
###### 2.5.1.1.27.6. [NodeController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-nodecontroller)
###### 2.5.1.1.27.7. [RenderNode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-rendernode)
###### 2.5.1.1.27.8. [AttributeUpdater](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-attributeupdater)
###### 2.5.1.1.27.9. [Content](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-content)
###### 2.5.1.1.27.10. [NodeContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-nodecontent)
###### 2.5.1.1.27.11. [Resource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-resource)
##### 2.5.1.2. 窗口管理

###### 2.5.1.2.1. [@ohos.window.floatView (闪控窗)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-floatview)
###### 2.5.1.2.2. [@ohos.PiPWindow (画中画窗口)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pipwindow)
###### 2.5.1.2.3. [@ohos.window.floatingBall (闪控球窗口)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-floatingball)
###### 2.5.1.2.4. @ohos.window (窗口)

###### 2.5.1.2.4.1. [模块描述](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window)
###### 2.5.1.2.4.2. [Functions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-f)
###### 2.5.1.2.4.3. [Interface (Window)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window)
###### 2.5.1.2.4.4. [Interface (WindowStage)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-windowstage)
###### 2.5.1.2.4.5. [Interfaces (其他)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-i)
###### 2.5.1.2.4.6. [Enums](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-e)
###### 2.5.1.2.4.7. [Types](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-t)
##### 2.5.1.3. 屏幕管理

###### 2.5.1.3.1. [@ohos.display (屏幕属性)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display)
###### 2.5.1.3.2. [@ohos.screenshot (屏幕截图)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-screenshot)
##### 2.5.1.4. 已停止维护的接口

###### 2.5.1.4.1. [@ohos.prompt (弹窗)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-prompt)
###### 2.5.1.4.2. [@system.app (应用上下文)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-app)
###### 2.5.1.4.3. [@system.configuration (应用配置)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-configuration)
###### 2.5.1.4.4. [@system.mediaquery (媒体查询)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-mediaquery)
###### 2.5.1.4.5. [@system.prompt (弹窗)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-prompt)
###### 2.5.1.4.6. [@system.router (页面路由)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-router)
###### 2.5.1.4.7. [XComponentNode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-xcomponentnode)
#### 2.5.2. ArkTS组件

##### 2.5.2.1. 通用事件

###### 2.5.2.1.1. 基础输入事件

###### 2.5.2.1.1.1. [触摸事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-touch)
###### 2.5.2.1.1.2. [鼠标事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-mouse-key)
###### 2.5.2.1.1.3. [轴事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-axis)
###### 2.5.2.1.1.4. [按键事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-key)
###### 2.5.2.1.1.5. [表冠事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-crown)
###### 2.5.2.1.1.6. [焦点轴事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-focus_axis)
###### 2.5.2.1.2. 交互响应事件

###### 2.5.2.1.2.1. [点击事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-click)
###### 2.5.2.1.2.2. [拖拽事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-drag-drop)
###### 2.5.2.1.2.3. [焦点事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-focus-event)
###### 2.5.2.1.2.4. [悬浮事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-hover)
###### 2.5.2.1.2.5. [组件快捷键事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-keyboardshortcut)
###### 2.5.2.1.2.6. [键盘判断事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-onneedsoftkeyboard)
###### 2.5.2.1.3. 交互事件分发控制

###### 2.5.2.1.3.1. [自定义事件拦截](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-on-touch-intercept)
###### 2.5.2.1.3.2. [自定义事件分发](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-on-child-touch-test)
###### 2.5.2.1.3.3. [全局基础输入事件监听](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-inputeventmonitor)
###### 2.5.2.1.4. 无障碍相关

###### 2.5.2.1.4.1. [无障碍控制操作](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-accessibility-event)
###### 2.5.2.1.4.2. [无障碍悬浮事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-accessibility-hover-event)
###### 2.5.2.1.5. 组件变化事件

###### 2.5.2.1.5.1. [挂载卸载事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-show-hide)
###### 2.5.2.1.5.2. [组件区域变化事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-area-change-event)
###### 2.5.2.1.5.3. [组件尺寸变化事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-size-change-event)
###### 2.5.2.1.5.4. [组件可见区域变化事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-visible-area-change-event)
##### 2.5.2.2. 通用属性

###### 2.5.2.2.1. 基础属性

###### 2.5.2.2.1.1. [组件标识](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-component-id)
###### 2.5.2.2.1.2. [分布式迁移标识](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-restoreid)
###### 2.5.2.2.1.3. [显隐控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-visibility)
###### 2.5.2.2.1.4. [背景设置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background)
###### 2.5.2.2.1.5. [浮层](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-overlay)
###### 2.5.2.2.1.6. [Z序控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-z-order)
###### 2.5.2.2.1.7. [隐私遮罩](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-obscured)
###### 2.5.2.2.1.8. [禁用反色能力](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-allow-force-dark)
###### 2.5.2.2.2. 布局与边框

###### 2.5.2.2.2.1. [尺寸设置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size)
###### 2.5.2.2.2.2. [位置设置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-location)
###### 2.5.2.2.2.3. [布局约束](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-layout-constraints)
###### 2.5.2.2.2.4. [Flex布局](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout)
###### 2.5.2.2.2.5. [安全区域](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-expand-safe-area)
###### 2.5.2.2.2.6. [组件级像素取整](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-pixelroundforcomponent)
###### 2.5.2.2.2.7. [页面级像素取整](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-pixelroundforpage)
###### 2.5.2.2.2.8. [边框设置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border)
###### 2.5.2.2.2.9. [图片边框设置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border-image)
###### 2.5.2.2.3. 视效与模糊

###### 2.5.2.2.3.1. [透明度设置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-opacity)
###### 2.5.2.2.3.2. [图形变换](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-transformation)
###### 2.5.2.2.3.3. [图像效果](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect)
###### 2.5.2.2.3.4. [形状裁剪](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sharp-clipping)
###### 2.5.2.2.3.5. [颜色渐变](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-gradient-color)
###### 2.5.2.2.3.6. [前景色设置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-foreground-color)
###### 2.5.2.2.3.7. [前景属性设置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-foreground-effect)
###### 2.5.2.2.3.8. [外描边设置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-outline)
###### 2.5.2.2.3.9. [视效设置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-filter-effect)
###### 2.5.2.2.3.10. [组件内容模糊](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-foreground-blur-style)
###### 2.5.2.2.3.11. [运动模糊](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-motionblur)
###### 2.5.2.2.3.12. [点击回弹效果](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-click-effect)
###### 2.5.2.2.3.13. [特效绘制合并](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-use-effect)
###### 2.5.2.2.3.14. [组件内容填充方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-renderfit)
###### 2.5.2.2.4. 交互属性

###### 2.5.2.2.4.1. [禁用控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-enable)
###### 2.5.2.2.4.2. [焦点控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-focus)
###### 2.5.2.2.4.3. [拖拽控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-drag-drop)
###### 2.5.2.2.4.4. [拖拽排序](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-drag-sorting)
###### 2.5.2.2.4.5. [悬浮态效果](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-hover-effect)
###### 2.5.2.2.4.6. [点击音效](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-click-sound)
####### 2.5.2.2.4.7. 触摸交互控制

###### 2.5.2.2.4.7.1. [触摸热区设置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-touch-target)
###### 2.5.2.2.4.7.2. [触摸测试控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-hit-test-behavior)
###### 2.5.2.2.4.7.3. [事件独占控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-monopolize-events)
###### 2.5.2.2.4.8. [鼠标光标控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-cursor)
###### 2.5.2.2.5. [多态样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-polymorphic-style)
###### 2.5.2.2.6. 弹窗控制

###### 2.5.2.2.6.1. [Popup控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup)
###### 2.5.2.2.6.2. [Tips控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-tips)
###### 2.5.2.2.6.3. [菜单控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-menu)
###### 2.5.2.2.7. [无障碍属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-accessibility)
###### 2.5.2.2.8. 模态转场设置

###### 2.5.2.2.8.1. [全屏模态转场](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-modal-transition)
###### 2.5.2.2.8.2. [半模态转场](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sheet-transition)
###### 2.5.2.2.9. 动态属性与自定义

###### 2.5.2.2.9.1. [动态属性设置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier)
###### 2.5.2.2.9.2. [动态手势设置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-gesture-modifier)
###### 2.5.2.2.9.3. [自定义绘制设置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-draw-modifier)
###### 2.5.2.2.9.4. [自定义内容](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-content-modifier)
###### 2.5.2.2.9.5. [自定义属性设置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-custom-property)
###### 2.5.2.2.9.6. [动态SymbolGlyphModifier属性设置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-symbolglyphmodifier)
###### 2.5.2.2.9.7. [属性操作工具](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-modifierutils)
###### 2.5.2.2.10. 其他

###### 2.5.2.2.10.1. [复用标识](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-reuse-id)
###### 2.5.2.2.10.2. [复用选项](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-reuse)
###### 2.5.2.2.10.3. [工具栏设置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-toolbar)
##### 2.5.2.3. 手势处理

###### 2.5.2.3.1. 绑定手势

###### 2.5.2.3.1.1. [绑定手势事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-settings)
###### 2.5.2.3.1.2. [设置组件绑定的手势](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-uigestureevent)
###### 2.5.2.3.1.3. [手势处理器](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesturehandler)
###### 2.5.2.3.2. 基础手势

###### 2.5.2.3.2.1. [TapGesture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-tapgesture)
###### 2.5.2.3.2.2. [LongPressGesture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-longpressgesture)
###### 2.5.2.3.2.3. [PanGesture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-pangesture)
###### 2.5.2.3.2.4. [PinchGesture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-pinchgesture)
###### 2.5.2.3.2.5. [RotationGesture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-rotationgesture)
###### 2.5.2.3.2.6. [SwipeGesture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-swipegesture)
###### 2.5.2.3.3. [GestureGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-combined-gestures)
###### 2.5.2.3.4. 手势控制

###### 2.5.2.3.4.1. [自定义手势判定](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-customize-judge)
###### 2.5.2.3.4.2. [手势拦截增强](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-blocking-enhancement)
###### 2.5.2.3.5. [手势公共接口](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-common)
##### 2.5.2.4. 行列与堆叠

###### 2.5.2.4.1. [Flex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex)
###### 2.5.2.4.2. [Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)
###### 2.5.2.4.3. [Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)
###### 2.5.2.4.4. [Stack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-stack)
###### 2.5.2.4.5. [RelativeContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-relativecontainer)
###### 2.5.2.4.6. [DynamicLayout](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-dynamiclayout)
###### 2.5.2.4.7. [ContainerReader](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-containerreader)
##### 2.5.2.5. 栅格与分栏

###### 2.5.2.5.1. [GridRow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow)
###### 2.5.2.5.2. [GridCol](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridcol)
###### 2.5.2.5.3. [ColumnSplit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-columnsplit)
###### 2.5.2.5.4. [RowSplit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-rowsplit)
###### 2.5.2.5.5. [SideBarContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-sidebarcontainer)
##### 2.5.2.6. 滚动与滑动

###### 2.5.2.6.1. [List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)
###### 2.5.2.6.2. [ListItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitem)
###### 2.5.2.6.3. [ListItemGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitemgroup)
###### 2.5.2.6.4. [ArcList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist)
###### 2.5.2.6.5. [ArcListItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclistitem)
###### 2.5.2.6.6. [Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid)
###### 2.5.2.6.7. [GridItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-griditem)
###### 2.5.2.6.8. [Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)
###### 2.5.2.6.9. [Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper)
###### 2.5.2.6.10. [ArcSwiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arcswiper)
###### 2.5.2.6.11. [WaterFlow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow)
###### 2.5.2.6.12. [FlowItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flowitem)
###### 2.5.2.6.13. [LazyVGridLayout](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-lazyvgridlayout)
###### 2.5.2.6.14. [LazyVWaterFlowLayout](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-lazyvwaterflowlayout)
###### 2.5.2.6.15. [ScrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-scrollbar)
###### 2.5.2.6.16. [Refresh](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-refresh)
###### 2.5.2.6.17. [ArcScrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-arcscrollbar)
###### 2.5.2.6.18. [滚动组件通用接口](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scrollable-common)
##### 2.5.2.7. 导航与切换

###### 2.5.2.7.1. [Indicator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-swiper-components-indicator)
###### 2.5.2.7.2. [Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation)
###### 2.5.2.7.3. [NavDestination](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination)
###### 2.5.2.7.4. [MultiNavigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-multinavigation)
###### 2.5.2.7.5. [Tabs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs)
###### 2.5.2.7.6. [TabContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabcontent)
###### 2.5.2.7.7. [ToolBarItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-toolbaritem)
##### 2.5.2.8. 按钮与选择

###### 2.5.2.8.1. [Button](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button)
###### 2.5.2.8.2. [Toggle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-toggle)
###### 2.5.2.8.3. [Checkbox](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-checkbox)
###### 2.5.2.8.4. [CheckboxGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-checkboxgroup)
###### 2.5.2.8.5. [UIPickerComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-ui-picker-component)
###### 2.5.2.8.6. [CalendarPicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-calendarpicker)
###### 2.5.2.8.7. [DatePicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-datepicker)
###### 2.5.2.8.8. [TextPicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textpicker)
###### 2.5.2.8.9. [TimePicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-timepicker)
###### 2.5.2.8.10. [Radio](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-radio)
###### 2.5.2.8.11. [Rating](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-rating)
###### 2.5.2.8.12. [Select](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-select)
###### 2.5.2.8.13. [Slider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-slider)
###### 2.5.2.8.14. [ArcButton](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton)
###### 2.5.2.8.15. [ArcSlider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcslider)
###### 2.5.2.8.16. [选择器（Picker）公共接口](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-picker-common)
##### 2.5.2.9. 文本与输入

###### 2.5.2.9.1. [Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)
###### 2.5.2.9.2. [TextArea](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea)
###### 2.5.2.9.3. [TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)
###### 2.5.2.9.4. [RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)
###### 2.5.2.9.5. [Search](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-search)
###### 2.5.2.9.6. [Span](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span)
###### 2.5.2.9.7. [ImageSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imagespan)
###### 2.5.2.9.8. [ContainerSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-containerspan)
###### 2.5.2.9.9. [SymbolSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan)
###### 2.5.2.9.10. [SymbolGlyph](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph)
###### 2.5.2.9.11. [Hyperlink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-hyperlink)
###### 2.5.2.9.12. [RichText](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richtext)
###### 2.5.2.9.13. [属性字符串](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string)
###### 2.5.2.9.14. [输入框类组件通用接口](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-text-style)
###### 2.5.2.9.15. [文本组件公共接口](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common)
##### 2.5.2.10. 图片与视频

###### 2.5.2.10.1. [Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image)
###### 2.5.2.10.2. [ImageAnimator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imageanimator)
###### 2.5.2.10.3. [Video](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-media-components-video)
###### 2.5.2.10.4. [图像类型定义](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-common)
###### 2.5.2.10.5. [SVG标签说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-svg)
###### 2.5.2.10.6. [SVG标签解析能力增强](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities)
##### 2.5.2.11. 信息展示

###### 2.5.2.11.1. [AlphabetIndexer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-alphabet-indexer)
###### 2.5.2.11.2. [ArcAlphabetIndexer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arc-alphabet-indexer)
###### 2.5.2.11.3. [Badge](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-badge)
###### 2.5.2.11.4. [Counter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-counter)
###### 2.5.2.11.5. [DataPanel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-datapanel)
###### 2.5.2.11.6. [Gauge](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-gauge)
###### 2.5.2.11.7. [LoadingProgress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-loadingprogress)
###### 2.5.2.11.8. [Marquee](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-marquee)
###### 2.5.2.11.9. [PatternLock](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-patternlock)
###### 2.5.2.11.10. [Progress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-progress)
###### 2.5.2.11.11. [QRCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-qrcode)
###### 2.5.2.11.12. [TextClock](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textclock)
###### 2.5.2.11.13. [TextTimer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-texttimer)
###### 2.5.2.11.14. [信息展示公共接口](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-information-display-common)
##### 2.5.2.12. 空白与分隔

###### 2.5.2.12.1. [Blank](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-blank)
###### 2.5.2.12.2. [Divider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-divider)
##### 2.5.2.13. 画布绘制

###### 2.5.2.13.1. [Canvas](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvas)
###### 2.5.2.13.2. [CanvasGradient](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvasgradient)
###### 2.5.2.13.3. [CanvasPattern](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvaspattern)
###### 2.5.2.13.4. [CanvasRenderingContext2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d)
###### 2.5.2.13.5. [DrawingRenderingContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawingrenderingcontext)
###### 2.5.2.13.6. [ImageBitmap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-imagebitmap)
###### 2.5.2.13.7. [ImageData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-imagedata)
###### 2.5.2.13.8. [Matrix2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-matrix2d)
###### 2.5.2.13.9. [OffscreenCanvas](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-offscreencanvas)
###### 2.5.2.13.10. [OffscreenCanvasRenderingContext2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-offscreencanvasrenderingcontext2d)
###### 2.5.2.13.11. [Path2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-path2d)
##### 2.5.2.14. 图形绘制

###### 2.5.2.14.1. [Circle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-circle)
###### 2.5.2.14.2. [Ellipse](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-ellipse)
###### 2.5.2.14.3. [Line](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-line)
###### 2.5.2.14.4. [Polyline](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-polyline)
###### 2.5.2.14.5. [Polygon](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-polygon)
###### 2.5.2.14.6. [Path](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-path)
###### 2.5.2.14.7. [Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-rect)
###### 2.5.2.14.8. [Shape](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-shape)
##### 2.5.2.15. 渲染绘制

###### 2.5.2.15.1. [XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-xcomponent)
###### 2.5.2.15.2. [Component3D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-component3d)
###### 2.5.2.15.3. [EmbeddedComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-embedded-component)
##### 2.5.2.16. 菜单

###### 2.5.2.16.1. [Menu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-menu)
###### 2.5.2.16.2. [MenuItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-menuitem)
###### 2.5.2.16.3. [MenuItemGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-menuitemgroup)
###### 2.5.2.16.4. [ContextMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-menu)
##### 2.5.2.17. 动画

###### 2.5.2.17.1. [属性动画 (animation)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-animatorproperty)
###### 2.5.2.17.2. [显式动画 (animateTo)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-explicit-animation)
###### 2.5.2.17.3. [关键帧动画 (keyframeAnimateTo)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-keyframeanimateto)
###### 2.5.2.17.4. [页面间转场 (pageTransition)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-page-transition-animation)
###### 2.5.2.17.5. [组件内转场 (transition)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-transition-animation-component)
###### 2.5.2.17.6. [共享元素转场 (sharedTransition)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-transition-animation-shared-elements)
###### 2.5.2.17.7. [组件内隐式共享元素转场 (geometryTransition)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-transition-animation-geometrytransition)
###### 2.5.2.17.8. [路径动画 (motionPath)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-motion-path-animation)
###### 2.5.2.17.9. [粒子动画 (Particle)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-particle-animation)
###### 2.5.2.17.10. [显式动画立即下发 (animateToImmediately)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-explicit-animatetoimmediately)
##### 2.5.2.18. 弹窗

###### 2.5.2.18.1. [警告弹窗 (AlertDialog)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-alert-dialog-box)
###### 2.5.2.18.2. [列表选择弹窗 (ActionSheet)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-action-sheet)
###### 2.5.2.18.3. [自定义弹窗 (CustomDialog)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-custom-dialog-box)
###### 2.5.2.18.4. [日历选择器弹窗 (CalendarPickerDialog)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-calendarpicker-dialog)
###### 2.5.2.18.5. [日期滑动选择器弹窗 (DatePickerDialog)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-datepicker-dialog)
###### 2.5.2.18.6. [时间滑动选择器弹窗 (TimePickerDialog)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-timepicker-dialog)
###### 2.5.2.18.7. [文本滑动选择器弹窗 (TextPickerDialog)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-textpicker-dialog)
###### 2.5.2.18.8. [弹出框 (Dialog)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-dialog)
##### 2.5.2.19. 卡片

###### 2.5.2.19.1. [FormLink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-formlink)
##### 2.5.2.20. 安全

###### 2.5.2.20.1. [安全控件通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-securitycomponent-attributes)
###### 2.5.2.20.2. [PasteButton](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-security-components-pastebutton)
###### 2.5.2.20.3. [SaveButton](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-security-components-savebutton)
##### 2.5.2.21. 主题

###### 2.5.2.21.1. [WithTheme](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-with-theme)
##### 2.5.2.22. AtomicService

###### 2.5.2.22.1. [AtomicServiceNavigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-atomicservicenavigation)
###### 2.5.2.22.2. [AtomicServiceSearch](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-atomicservicesearch)
###### 2.5.2.22.3. [AtomicServiceTabs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-atomicservicetabs)
###### 2.5.2.22.4. [AtomicServiceWeb](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-atomicserviceweb)
###### 2.5.2.22.5. [InterstitialDialogAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-interstitialdialogaction)
###### 2.5.2.22.6. [HalfScreenLaunchComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-halfscreenlaunchcomponent)
###### 2.5.2.22.7. [NavPushPathHelper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-navpushpathhelper)
##### 2.5.2.23. 自定义占位组件

###### 2.5.2.23.1. [NodeContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-nodecontainer)
###### 2.5.2.23.2. [ContentSlot](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-contentslot)
##### 2.5.2.24. 自定义组件

###### 2.5.2.24.1. [自定义组件的生命周期](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-lifecycle)
###### 2.5.2.24.2. [自定义组件的生命周期（推荐）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-new-lifecycle)
###### 2.5.2.24.3. [自定义组件的自定义布局](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-layout)
###### 2.5.2.24.4. [自定义组件内置方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-api)
###### 2.5.2.24.5. [自定义组件参数](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-parameter)
###### 2.5.2.24.6. [@Entry：页面入口](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-entry)
###### 2.5.2.24.7. 组件扩展装饰器

###### 2.5.2.24.7.1. [定义可动画属性 (@AnimatableExtend)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-animatable-extend)
###### 2.5.2.24.7.2. [wrapBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-wrapbuilder)
###### 2.5.2.24.7.3. [mutableBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-mutablebuilder)
##### 2.5.2.25. 组件预览

###### 2.5.2.25.1. [组件预览](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-previewer)
##### 2.5.2.26. 系统预置UI组件库

###### 2.5.2.26.1. [Chip](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-chip)
###### 2.5.2.26.2. [ChipGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-chipgroup)
###### 2.5.2.26.3. [ComposeListItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-composelistitem)
###### 2.5.2.26.4. [ComposeTitleBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-composetitlebar)
###### 2.5.2.26.5. [DownloadFileButton](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-downloadfilebutton)
###### 2.5.2.26.6. [DialogV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-dialogv2)
###### 2.5.2.26.7. [EditableTitleBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-editabletitlebar)
###### 2.5.2.26.8. [ExceptionPrompt](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-exceptionprompt)
###### 2.5.2.26.9. [Filter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-filter)
###### 2.5.2.26.10. [FolderStack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-folderstack)
###### 2.5.2.26.11. [FoldSplitContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-foldsplitcontainer)
###### 2.5.2.26.12. [FormMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-formmenu)
###### 2.5.2.26.13. [FullScreenLaunchComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-fullscreenlaunchcomponent)
###### 2.5.2.26.14. [GridObjectSortComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-gridobjectsortcomponent)
###### 2.5.2.26.15. [Popup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-popup)
###### 2.5.2.26.16. [ProgressButton](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-progressbutton)
###### 2.5.2.26.17. [ProgressButtonV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-progressbuttonv2)
###### 2.5.2.26.18. [SegmentButton](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-segmentbutton)
###### 2.5.2.26.19. [SegmentButtonV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-segmentbuttonv2)
###### 2.5.2.26.20. [SelectTitleBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-selecttitlebar)
###### 2.5.2.26.21. [SelectionMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-selectionmenu)
###### 2.5.2.26.22. [SplitLayout](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-splitlayout)
###### 2.5.2.26.23. [SubHeader](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-subheader)
###### 2.5.2.26.24. [SubHeaderV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-subheaderv2)
###### 2.5.2.26.25. [SwipeRefresher](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-swiperefresher)
###### 2.5.2.26.26. [TabTitleBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-tabtitlebar)
###### 2.5.2.26.27. [ToolBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-toolbar)
###### 2.5.2.26.28. [ToolBarV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-toolbarv2)
###### 2.5.2.26.29. [TreeView](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-treeview)
###### 2.5.2.26.30. [advanced.Counter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-counter)
##### 2.5.2.27. 状态管理与渲染控制

###### 2.5.2.27.1. [应用级变量的状态管理](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management)
###### 2.5.2.27.2. [状态管理V1装饰器参数](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-v1-parameter)
###### 2.5.2.27.3. [状态变量变化监听](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-watch-monitor)
###### 2.5.2.27.4. [内置环境变量说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-environment-variables)
###### 2.5.2.27.5. [ForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-foreach)
###### 2.5.2.27.6. [LazyForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-lazyforeach)
###### 2.5.2.27.7. [Repeat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-repeat)
##### 2.5.2.28. 响应式环境变量

###### 2.5.2.28.1. [@Env：环境变量](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-env-system-property)
##### 2.5.2.29. 公共定义

###### 2.5.2.29.1. [基础类型定义](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types)
###### 2.5.2.29.2. [像素单位](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-pixel-units)
###### 2.5.2.29.3. [枚举说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums)
###### 2.5.2.29.4. [设置事件回调](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-uicommonevent)
##### 2.5.2.30. 已停止维护的组件与接口

###### 2.5.2.30.1. [GridContainer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridcontainer)
###### 2.5.2.30.2. [Panel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-panel)
###### 2.5.2.30.3. [NavRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navrouter)
###### 2.5.2.30.4. [Navigator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-navigator)
###### 2.5.2.30.5. [点击控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-click)
###### 2.5.2.30.6. [栅格设置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-grid)
###### 2.5.2.30.7. [Stepper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-stepper)
###### 2.5.2.30.8. [StepperItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-stepperitem)
#### 2.5.3. JS组件

##### 2.5.3.1. 兼容JS的类Web开发范式（ArkUI.Full）

###### 2.5.3.1.1. 组件通用信息

###### 2.5.3.1.1.1. [通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-attributes)
###### 2.5.3.1.1.2. [通用样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-styles)
###### 2.5.3.1.1.3. [通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-events)
###### 2.5.3.1.1.4. [通用方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-methods)
###### 2.5.3.1.1.5. [动画样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-animation)
###### 2.5.3.1.1.6. [渐变样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-gradient)
###### 2.5.3.1.1.7. [转场样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-transition)
###### 2.5.3.1.1.8. [媒体查询](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-mediaquery)
###### 2.5.3.1.1.9. [自定义字体样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-customizing-font)
###### 2.5.3.1.1.10. [原子布局](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-atomic-layout)
###### 2.5.3.1.2. 容器组件

###### 2.5.3.1.2.1. [badge](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-badge)
###### 2.5.3.1.2.2. [dialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-dialog)
###### 2.5.3.1.2.3. [div](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-div)
###### 2.5.3.1.2.4. [form](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-form)
###### 2.5.3.1.2.5. [list](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-list)
###### 2.5.3.1.2.6. [list-item](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-list-item)
###### 2.5.3.1.2.7. [list-item-group](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-list-item-group)
###### 2.5.3.1.2.8. [panel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-panel)
###### 2.5.3.1.2.9. [popup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-popup)
###### 2.5.3.1.2.10. [refresh](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-refresh)
###### 2.5.3.1.2.11. [stack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-stack)
###### 2.5.3.1.2.12. [stepper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-stepper)
###### 2.5.3.1.2.13. [stepper-item](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-stepper-item)
###### 2.5.3.1.2.14. [swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-swiper)
###### 2.5.3.1.2.15. [tabs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-tabs)
###### 2.5.3.1.2.16. [tab-bar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-tab-bar)
###### 2.5.3.1.2.17. [tab-content](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-tab-content)
###### 2.5.3.1.3. 基础组件

###### 2.5.3.1.3.1. [button](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-button)
###### 2.5.3.1.3.2. [chart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-chart)
###### 2.5.3.1.3.3. [divider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-divider)
###### 2.5.3.1.3.4. [image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-image)
###### 2.5.3.1.3.5. [image-animator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-image-animator)
###### 2.5.3.1.3.6. [input](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-input)
###### 2.5.3.1.3.7. [label](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-label)
###### 2.5.3.1.3.8. [marquee](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-marquee)
###### 2.5.3.1.3.9. [menu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-menu)
###### 2.5.3.1.3.10. [option](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-option)
###### 2.5.3.1.3.11. [picker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-picker)
###### 2.5.3.1.3.12. [picker-view](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-picker-view)
###### 2.5.3.1.3.13. [piece](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-piece)
###### 2.5.3.1.3.14. [progress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-progress)
###### 2.5.3.1.3.15. [qrcode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-qrcode)
###### 2.5.3.1.3.16. [rating](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-rating)
###### 2.5.3.1.3.17. [richtext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-richtext)
###### 2.5.3.1.3.18. [search](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-search)
###### 2.5.3.1.3.19. [select](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-select)
###### 2.5.3.1.3.20. [slider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-slider)
###### 2.5.3.1.3.21. [span](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-span)
###### 2.5.3.1.3.22. [switch](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-switch)
###### 2.5.3.1.3.23. [text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-text)
###### 2.5.3.1.3.24. [textarea](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-textarea)
###### 2.5.3.1.3.25. [toolbar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-toolbar)
###### 2.5.3.1.3.26. [toolbar-item](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-toolbar-item)
###### 2.5.3.1.3.27. [toggle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-toggle)
###### 2.5.3.1.3.28. [web](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-web)
###### 2.5.3.1.3.29. [xcomponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-xcomponent)
###### 2.5.3.1.4. 媒体组件

###### 2.5.3.1.4.1. [video](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-media-video)
###### 2.5.3.1.5. 画布组件

###### 2.5.3.1.5.1. [canvas组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvas)
###### 2.5.3.1.5.2. [CanvasRenderingContext2D对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvasrenderingcontext2d)
###### 2.5.3.1.5.3. [Image对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-image)
###### 2.5.3.1.5.4. [CanvasGradient对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvasgradient)
###### 2.5.3.1.5.5. [ImageData对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-imagedata)
###### 2.5.3.1.5.6. [Path2D对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-path2d)
###### 2.5.3.1.5.7. [ImageBitmap对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-imagebitmap)
###### 2.5.3.1.5.8. [OffscreenCanvas对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-offscreencanvas)
###### 2.5.3.1.5.9. [OffscreenCanvasRenderingContext2D对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-offscreencanvasrenderingcontext2d)
###### 2.5.3.1.6. 栅格组件

###### 2.5.3.1.6.1. [基本概念](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-grid-basic-concepts)
###### 2.5.3.1.6.2. [grid-container](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-grid-container)
###### 2.5.3.1.6.3. [grid-row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-grid-row)
###### 2.5.3.1.6.4. [grid-col](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-grid-col)
###### 2.5.3.1.7. svg组件

###### 2.5.3.1.7.1. [通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-common-attributes)
###### 2.5.3.1.7.2. [svg](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg)
###### 2.5.3.1.7.3. [rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-rect)
###### 2.5.3.1.7.4. [circle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-circle)
###### 2.5.3.1.7.5. [ellipse](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-ellipse)
###### 2.5.3.1.7.6. [path](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-path)
###### 2.5.3.1.7.7. [line](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-line)
###### 2.5.3.1.7.8. [polyline](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-polyline)
###### 2.5.3.1.7.9. [polygon](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-polygon)
###### 2.5.3.1.7.10. [text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-text)
###### 2.5.3.1.7.11. [tspan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-tspan)
###### 2.5.3.1.7.12. [textPath](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-textpath)
###### 2.5.3.1.7.13. [animate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animate)
###### 2.5.3.1.7.14. [animateMotion](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animatemotion)
###### 2.5.3.1.7.15. [animateTransform](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animatetransform)
###### 2.5.3.1.8. 自定义组件

###### 2.5.3.1.8.1. [自定义组件的基本用法](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-custom-basic-usage)
###### 2.5.3.1.8.2. [数据传递与处理](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-custom-props)
###### 2.5.3.1.8.3. [继承样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-custom-style)
###### 2.5.3.1.8.4. [slot插槽](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-custom-slot)
###### 2.5.3.1.8.5. [生命周期定义](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-custom-lifecycle)
###### 2.5.3.1.9. 全局接口

###### 2.5.3.1.9.1. [旋转表冠事件监听](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-monitorcrownevents)
###### 2.5.3.1.10. [动态创建组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-create-elements)
###### 2.5.3.1.11. [数据类型说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-appendix-types)
##### 2.5.3.2. 兼容JS的类Web开发范式（ArkUI.Lite）

###### 2.5.3.2.1. 框架说明

###### 2.5.3.2.1.1. [文件组织](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-file)
###### 2.5.3.2.1.2. [js标签配置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-js-tag)
###### 2.5.3.2.1.3. [app.js](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-js-file)
###### 2.5.3.2.1.4. [生命周期](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-lifecycle)
###### 2.5.3.2.1.5. [多语言支持](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-localization)
####### 2.5.3.2.1.6. 语法

###### 2.5.3.2.1.6.1. [HML语法参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-syntax-hml)
###### 2.5.3.2.1.6.2. [CSS语法参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-syntax-css)
###### 2.5.3.2.1.6.3. [JS语法参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-syntax-js)
###### 2.5.3.2.2. 组件通用信息

###### 2.5.3.2.2.1. [通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-common-events)
###### 2.5.3.2.2.2. [通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-common-attributes)
###### 2.5.3.2.2.3. [通用样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-common-styles)
###### 2.5.3.2.2.4. [动画样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-common-animation)
###### 2.5.3.2.2.5. [媒体查询](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-common-mediaquery)
###### 2.5.3.2.3. 容器组件

###### 2.5.3.2.3.1. [div](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-container-div)
###### 2.5.3.2.3.2. [list](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-container-list)
###### 2.5.3.2.3.3. [list-item](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-container-list-item)
###### 2.5.3.2.3.4. [stack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-container-stack)
###### 2.5.3.2.3.5. [swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-container-swiper)
###### 2.5.3.2.4. 基础组件

###### 2.5.3.2.4.1. [chart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-chart)
###### 2.5.3.2.4.2. [image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-image)
###### 2.5.3.2.4.3. [image-animator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-image-animator)
###### 2.5.3.2.4.4. [input](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-input)
###### 2.5.3.2.4.5. [marquee](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-marquee)
###### 2.5.3.2.4.6. [picker-view](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-picker-view)
###### 2.5.3.2.4.7. [progress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-progress)
###### 2.5.3.2.4.8. [qrcode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-qrcode)
###### 2.5.3.2.4.9. [slider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-slider)
###### 2.5.3.2.4.10. [switch](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-switch)
###### 2.5.3.2.4.11. [text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-text)
###### 2.5.3.2.5. 画布组件

###### 2.5.3.2.5.1. [canvas组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-canvas-canvas)
###### 2.5.3.2.5.2. [CanvasRenderingContext2D对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-canvas-canvasrenderingcontext2d)
###### 2.5.3.2.6. 全局接口

###### 2.5.3.2.6.1. [旋转表冠事件监听](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-common-monitorcrownevents)
##### 2.5.3.3. JS服务卡片UI组件

###### 2.5.3.3.1. 框架说明

###### 2.5.3.3.1.1. [文件组织](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-file)
####### 2.5.3.3.1.2. 语法

###### 2.5.3.3.1.2.1. [HML语法参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-syntax-hml)
###### 2.5.3.3.1.2.2. [CSS语法参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-syntax-css)
###### 2.5.3.3.1.3. [多语言支持](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-multiple-languages)
###### 2.5.3.3.1.4. [版本兼容适配](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-version-compatibility)
###### 2.5.3.3.1.5. [设置主题样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-theme)
###### 2.5.3.3.2. 组件通用信息

###### 2.5.3.3.2.1. [通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-attributes)
###### 2.5.3.3.2.2. [通用样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-styles)
###### 2.5.3.3.2.3. [通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-events)
###### 2.5.3.3.2.4. [渐变样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-gradient)
###### 2.5.3.3.2.5. [媒体查询](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-mediaquery)
###### 2.5.3.3.2.6. [自定义字体样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-customizing-font)
###### 2.5.3.3.2.7. [无障碍](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-accessibility)
###### 2.5.3.3.2.8. [原子布局](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-atomic-layout)
###### 2.5.3.3.3. 容器组件

###### 2.5.3.3.3.1. [badge](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-container-badge)
###### 2.5.3.3.3.2. [div](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-container-div)
###### 2.5.3.3.3.3. [list](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-container-list)
###### 2.5.3.3.3.4. [list-item](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-container-list-item)
###### 2.5.3.3.3.5. [stack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-container-stack)
###### 2.5.3.3.3.6. [swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-container-swiper)
###### 2.5.3.3.4. 基础组件

###### 2.5.3.3.4.1. [button](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-basic-button)
###### 2.5.3.3.4.2. [calendar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-basic-calendar)
###### 2.5.3.3.4.3. [chart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-basic-chart)
###### 2.5.3.3.4.4. [clock](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-basic-clock)
###### 2.5.3.3.4.5. [divider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-basic-divider)
###### 2.5.3.3.4.6. [image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-basic-image)
###### 2.5.3.3.4.7. [input](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-basic-input)
###### 2.5.3.3.4.8. [progress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-basic-progress)
###### 2.5.3.3.4.9. [span](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-basic-span)
###### 2.5.3.3.4.10. [text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-basic-text)
###### 2.5.3.3.5. [自定义组件使用说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-custom-basic-usage)
###### 2.5.3.3.6. [数据类型说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-appendix-types)
#### 2.5.4. C API

##### 2.5.4.1. 模块

###### 2.5.4.1.1. [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
###### 2.5.4.1.2. [ArkUI_Accessibility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility)
###### 2.5.4.1.3. [OH_NativeXComponent Native XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent)
###### 2.5.4.1.4. [ArkUI_EventModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-eventmodule)
###### 2.5.4.1.5. [WindowManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager)
###### 2.5.4.1.6. [OH_DisplayManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-displaymanager)
###### 2.5.4.1.7. [ArkUI_RenderNodeUtils](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-rendernodeutils)
##### 2.5.4.2. 头文件

###### 2.5.4.2.1. [drag_and_drop.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drag-and-drop-h)
###### 2.5.4.2.2. [drawable_descriptor.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawable-descriptor-h)
###### 2.5.4.2.3. [native_animate.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-animate-h)
###### 2.5.4.2.4. [native_dialog.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-dialog-h)
###### 2.5.4.2.5. [native_gesture.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-gesture-h)
###### 2.5.4.2.6. [native_interface.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-h)
###### 2.5.4.2.7. [native_interface_accessibility.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-accessibility-h)
###### 2.5.4.2.8. [native_interface_focus.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-focus-h)
###### 2.5.4.2.9. [native_interface_xcomponent.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-xcomponent-h)
###### 2.5.4.2.10. [native_key_event.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-key-event-h)
###### 2.5.4.2.11. native_node.h

###### 2.5.4.2.11.1. [ArkUI_NodeAttributeType（基础属性）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-base)
###### 2.5.4.2.11.2. [ArkUI_NodeAttributeType（通用属性）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-common)
###### 2.5.4.2.11.3. [ArkUI_NodeAttributeType（布局属性）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-layoutattributes)
###### 2.5.4.2.11.4. [ArkUI_NodeAttributeType（布局类组件相关属性）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-layoutcomponent)
###### 2.5.4.2.11.5. [ArkUI_NodeAttributeType（动效、视效相关属性）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-animator)
###### 2.5.4.2.11.6. [ArkUI_NodeAttributeType（交互类相关属性）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-interaction)
###### 2.5.4.2.11.7. [ArkUI_NodeAttributeType（表单类组件相关属性）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-form)
###### 2.5.4.2.11.8. [ArkUI_NodeAttributeType（滚动容器类组件相关属性）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-scrollablecontainer)
###### 2.5.4.2.11.9. [ArkUI_NodeAttributeType（导航类组件相关属性）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-navigationrelatedcomponents)
###### 2.5.4.2.11.10. [ArkUI_NodeAttributeType（信息展示类组件相关属性）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-informationdisplay)
###### 2.5.4.2.11.11. [ArkUI_NodeAttributeType（信息选择类组件相关属性）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-informationselection)
###### 2.5.4.2.11.12. [ArkUI_NodeAttributeType（无障碍相关属性）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-accessibility)
###### 2.5.4.2.11.13. [ArkUI_NodeAttributeType（文本显示类组件相关属性）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-text)
###### 2.5.4.2.11.14. [ArkUI_NodeAttributeType（文本输入类组件相关属性）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-textinputcategory)
###### 2.5.4.2.11.15. [ArkUI_NodeAttributeType（富文本类组件相关属性）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-richeditor)
###### 2.5.4.2.11.16. [ArkUI_NodeAttributeType（图类组件相关属性）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-image)
###### 2.5.4.2.11.17. [ArkUI_NodeAttributeType（XComponent组件相关属性）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-xcomponent)
###### 2.5.4.2.11.18. [ArkUI_NodeAttributeType（EmbeddedComponent组件相关属性）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-embeddedcomponent)
###### 2.5.4.2.11.19. [ArkUI_NodeAttributeType（其他）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-other)
###### 2.5.4.2.12. [native_node_napi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-napi-h)
###### 2.5.4.2.13. [native_render.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-render-h)
###### 2.5.4.2.14. [native_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h)
###### 2.5.4.2.15. [native_xcomponent_key_event.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-xcomponent-key-event-h)
###### 2.5.4.2.16. [styled_string.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h)
###### 2.5.4.2.17. [ui_input_event.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ui-input-event-h)
###### 2.5.4.2.18. [oh_window.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-window-h)
###### 2.5.4.2.19. [oh_window_comm.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-window-comm-h)
###### 2.5.4.2.20. [oh_window_event_filter.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-window-event-filter-h)
###### 2.5.4.2.21. [oh_window_pip.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-window-pip-h)
###### 2.5.4.2.22. [oh_display_capture.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-capture-h)
###### 2.5.4.2.23. [oh_display_info.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h)
###### 2.5.4.2.24. [oh_display_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h)
##### 2.5.4.3. 结构体

###### 2.5.4.3.1. [ArkUI_NodeEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodeevent)
###### 2.5.4.3.2. [ArkUI_Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-context)
###### 2.5.4.3.3. [ArkUI_Context*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-context8h)
###### 2.5.4.3.4. [ArkUI_DragEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-dragevent)
###### 2.5.4.3.5. [ArkUI_DragPreviewOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-dragpreviewoption)
###### 2.5.4.3.6. [ArkUI_DragAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-dragaction)
###### 2.5.4.3.7. [ArkUI_DragAndDropInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-draganddropinfo)
###### 2.5.4.3.8. [ArkUI_DrawableDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-drawabledescriptor)
###### 2.5.4.3.9. [ArkUI_DrawableDescriptor_AnimationController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-drawabledescriptoranimationcontroller)
###### 2.5.4.3.10. [OH_ArkUI_FontConfigs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-fontconfigs)
###### 2.5.4.3.11. [OH_ArkUI_FontWeightConfigs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-fontweightconfigs)
###### 2.5.4.3.12. [OH_PixelmapNative*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-pixelmapnative8h)
###### 2.5.4.3.13. [ArkUI_ExpectedFrameRateRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-expectedframeraterange)
###### 2.5.4.3.14. [ArkUI_AnimateCompleteCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatecompletecallback)
###### 2.5.4.3.15. [ArkUI_NativeAnimateAPI_1](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1)
###### 2.5.4.3.16. [ArkUI_AnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animateoption)
###### 2.5.4.3.17. [ArkUI_Curve](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-curve)
###### 2.5.4.3.18. [ArkUI_Curve*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-curve8h)
###### 2.5.4.3.19. [ArkUI_KeyframeAnimateOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-keyframeanimateoption)
###### 2.5.4.3.20. [ArkUI_AnimatorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption)
###### 2.5.4.3.21. [ArkUI_Animator*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animator8h)
###### 2.5.4.3.22. [ArkUI_AnimatorEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatorevent)
###### 2.5.4.3.23. [ArkUI_AnimatorOnFrameEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoronframeevent)
###### 2.5.4.3.24. [ArkUI_TransitionEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-transitioneffect)
###### 2.5.4.3.25. [ArkUI_NativeDialogAPI_1](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1)
###### 2.5.4.3.26. [ArkUI_NativeDialogAPI_2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-2)
###### 2.5.4.3.27. [ArkUI_NativeDialogAPI_3](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-3)
###### 2.5.4.3.28. [ArkUI_DialogDismissEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-dialogdismissevent)
###### 2.5.4.3.29. [ArkUI_CustomDialogOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-customdialogoptions)
###### 2.5.4.3.30. [ArkUI_NativeGestureAPI_1](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativegestureapi-1)
###### 2.5.4.3.31. [ArkUI_NativeGestureAPI_2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativegestureapi-2)
###### 2.5.4.3.32. [ArkUI_GestureRecognizer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-gesturerecognizer)
###### 2.5.4.3.33. [ArkUI_GestureInterruptInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-gestureinterruptinfo)
###### 2.5.4.3.34. [ArkUI_GestureEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-gestureevent)
###### 2.5.4.3.35. [ArkUI_GestureEventTargetInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-gestureeventtargetinfo)
###### 2.5.4.3.36. [ArkUI_GestureCollectInterceptInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-gesturecollectinterceptinfo)
###### 2.5.4.3.37. [ArkUI_ParallelInnerGestureEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-parallelinnergestureevent)
###### 2.5.4.3.38. [ArkUI_TouchRecognizer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-touchrecognizer)
###### 2.5.4.3.39. [ArkUI_TouchRecognizer*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-touchrecognizerhandle)
###### 2.5.4.3.40. [ArkUI_TouchRecognizerHandle*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-touchrecognizerhandlearray)
###### 2.5.4.3.41. [ArkUI_GestureRecognizer*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-gesturerecognizerhandle)
###### 2.5.4.3.42. [ArkUI_GestureRecognizerHandle*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-gesturerecognizerhandlearray)
###### 2.5.4.3.43. [ArkUI_AccessibleAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessibleaction)
###### 2.5.4.3.44. [ArkUI_AccessibleRect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessiblerect)
###### 2.5.4.3.45. [ArkUI_AccessibleRangeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessiblerangeinfo)
###### 2.5.4.3.46. [ArkUI_AccessibleGridInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessiblegridinfo)
###### 2.5.4.3.47. [ArkUI_AccessibleGridItemInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessiblegriditeminfo)
###### 2.5.4.3.48. [ArkUI_AccessibilityProviderCallbacks](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessibilityprovidercallbacks)
###### 2.5.4.3.49. [ArkUI_AccessibilityProviderCallbacksWithInstance](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessibilityprovidercallbackswithinstance)
###### 2.5.4.3.50. [ArkUI_AccessibilityElementInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessibilityelementinfo)
###### 2.5.4.3.51. [ArkUI_AccessibilityEventInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessibilityeventinfo)
###### 2.5.4.3.52. [ArkUI_AccessibilityProvider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessibilityprovider)
###### 2.5.4.3.53. [ArkUI_AccessibilityActionArguments](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessibilityactionarguments)
###### 2.5.4.3.54. [ArkUI_AccessibilityElementInfoList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessibilityelementinfolist)
###### 2.5.4.3.55. [OH_NativeXComponent_HistoricalPoint](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-historicalpoint)
###### 2.5.4.3.56. [OH_NativeXComponent_TouchPoint](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-touchpoint)
###### 2.5.4.3.57. [OH_NativeXComponent_TouchEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-touchevent)
###### 2.5.4.3.58. [OH_NativeXComponent_MouseEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-mouseevent)
###### 2.5.4.3.59. [OH_NativeXComponent_Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-callback)
###### 2.5.4.3.60. [OH_NativeXComponent_MouseEvent_Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-mouseevent-callback)
###### 2.5.4.3.61. [OH_NativeXComponent_ExpectedRateRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-expectedraterange)
###### 2.5.4.3.62. [OH_NativeXComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent)
###### 2.5.4.3.63. [OH_NativeXComponent_KeyEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-keyevent)
###### 2.5.4.3.64. [OH_NativeXComponent_ExtraMouseEventInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-extramouseeventinfo)
###### 2.5.4.3.65. [OH_ArkUI_SurfaceHolder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-arkui-surfaceholder)
###### 2.5.4.3.66. [OH_ArkUI_SurfaceCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-arkui-surfacecallback)
###### 2.5.4.3.67. [NativeWindow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-nativewindow)
###### 2.5.4.3.68. [ArkUI_XComponentSurfaceConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-arkui-xcomponentsurfaceconfig)
###### 2.5.4.3.69. [ArkUI_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)
###### 2.5.4.3.70. [ArkUI_NodeComponentEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodecomponentevent)
###### 2.5.4.3.71. [ArkUI_StringAsyncEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-stringasyncevent)
###### 2.5.4.3.72. [ArkUI_TextChangeEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textchangeevent)
###### 2.5.4.3.73. [ArkUI_NativeNodeAPI_1](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1)
###### 2.5.4.3.74. [OH_ArkUI_TextEditorChangeEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-texteditorchangeevent)
###### 2.5.4.3.75. [ArkUI_NodeCustomEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodecustomevent)
###### 2.5.4.3.76. [ArkUI_NodeAdapter*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodeadapter8h)
###### 2.5.4.3.77. [ArkUI_NodeAdapterEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodeadapterevent)
###### 2.5.4.3.78. [ArkUI_NodeContentEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodecontentevent)
###### 2.5.4.3.79. [ArkUI_ContextCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-contextcallback)
###### 2.5.4.3.80. [ArkUI_NumberValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-numbervalue)
###### 2.5.4.3.81. [ARKUI_TextPickerRangeContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textpickerrangecontent)
###### 2.5.4.3.82. [ARKUI_TextPickerCascadeRangeContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textpickercascaderangecontent)
###### 2.5.4.3.83. [ArkUI_ColorStop](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-colorstop)
###### 2.5.4.3.84. [ArkUI_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-rect)
###### 2.5.4.3.85. [ArkUI_IntSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-intsize)
###### 2.5.4.3.86. [ArkUI_IntOffset](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-intoffset)
###### 2.5.4.3.87. [ArkUI_Margin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-margin)
###### 2.5.4.3.88. [ArkUI_Matrix4](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-matrix4)
###### 2.5.4.3.89. [ArkUI_Matrix4RotationOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-matrix4rotationoptions)
###### 2.5.4.3.90. [ArkUI_Matrix4ScaleOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-matrix4scaleoptions)
###### 2.5.4.3.91. [ArkUI_Matrix4TranslationOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-matrix4translationoptions)
###### 2.5.4.3.92. [ArkUI_PointF](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-pointf)
###### 2.5.4.3.93. [ArkUI_TranslationOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-translationoptions)
###### 2.5.4.3.94. [ArkUI_ScaleOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-scaleoptions)
###### 2.5.4.3.95. [ArkUI_RotationOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-rotationoptions)
###### 2.5.4.3.96. [ArkUI_NativeDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog)
###### 2.5.4.3.97. [ArkUI_LayoutConstraint](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-layoutconstraint)
###### 2.5.4.3.98. [ArkUI_DrawContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-drawcontext)
###### 2.5.4.3.99. [ArkUI_Node](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node-descriptor)
###### 2.5.4.3.100. [ArkUI_Node*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h)
###### 2.5.4.3.101. [ArkUI_NativeDialog*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h)
###### 2.5.4.3.102. [ArkUI_WaterFlowSectionOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-waterflowsectionoption)
###### 2.5.4.3.103. [ArkUI_ListItemSwipeActionItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-listitemswipeactionitem)
###### 2.5.4.3.104. [ArkUI_ListItemSwipeActionOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-listitemswipeactionoption)
###### 2.5.4.3.105. [ArkUI_NodeContent*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodecontent8h)
###### 2.5.4.3.106. [ArkUI_AlignmentRuleOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-alignmentruleoption)
###### 2.5.4.3.107. [ArkUI_GuidelineOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-guidelineoption)
###### 2.5.4.3.108. [ArkUI_BarrierOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-barrieroption)
###### 2.5.4.3.109. [ArkUI_ImageAnimatorFrameInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-imageanimatorframeinfo)
###### 2.5.4.3.110. [ArkUI_ListChildrenMainSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-listchildrenmainsize)
###### 2.5.4.3.111. [ArkUI_ProgressLinearStyleOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-progresslinearstyleoption)
###### 2.5.4.3.112. [ArkUI_CustomProperty](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-customproperty)
###### 2.5.4.3.113. [ArkUI_HostWindowInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-hostwindowinfo)
###### 2.5.4.3.114. [ArkUI_ActiveChildrenInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-activechildreninfo)
###### 2.5.4.3.115. [ArkUI_CrossLanguageOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-crosslanguageoption)
###### 2.5.4.3.116. [AbilityBase_Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-abilitybase-want)
###### 2.5.4.3.117. [ArkUI_EmbeddedComponentOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-embeddedcomponentoption)
###### 2.5.4.3.118. [ArkUI_AccessibilityState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-accessibilitystate)
###### 2.5.4.3.119. [ArkUI_AccessibilityValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-accessibilityvalue)
###### 2.5.4.3.120. [ArkUI_SystemFontStyleEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-systemfontstyleevent)
###### 2.5.4.3.121. [ArkUI_CustomSpanMeasureInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-customspanmeasureinfo)
###### 2.5.4.3.122. [ArkUI_CustomSpanMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-customspanmetrics)
###### 2.5.4.3.123. [ArkUI_CustomSpanDrawInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-customspandrawinfo)
###### 2.5.4.3.124. [ArkUI_SwiperIndicator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-swiperindicator)
###### 2.5.4.3.125. [ArkUI_SwiperDigitIndicator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-swiperdigitindicator)
###### 2.5.4.3.126. [ArkUI_SwiperArrowStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-swiperarrowstyle)
###### 2.5.4.3.127. [ArkUI_StyledString_Descriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-styledstring-descriptor)
###### 2.5.4.3.128. [ArkUI_SnapshotOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-snapshotoptions)
###### 2.5.4.3.129. [ArkUI_TextPickerRangeContentArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textpickerrangecontentarray)
###### 2.5.4.3.130. [ArkUI_TextCascadePickerRangeContentArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textcascadepickerrangecontentarray)
###### 2.5.4.3.131. [ArkUI_SelectionOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-selectionoptions)
###### 2.5.4.3.132. [ArkUI_VisibleAreaEventOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-visibleareaeventoptions)
###### 2.5.4.3.133. [ArkUI_PositionEdges](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-positionedges)
###### 2.5.4.3.134. [ArkUI_PixelRoundPolicy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-pixelroundpolicy)
###### 2.5.4.3.135. [ArkUI_MotionPathOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-motionpathoptions)
###### 2.5.4.3.136. [ArkUI_StyledString](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-styledstring)
###### 2.5.4.3.137. [OH_ArkUI_SpanStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-spanstyle)
###### 2.5.4.3.138. [OH_ArkUI_ImageAttachment](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-imageattachment)
###### 2.5.4.3.139. [OH_ArkUI_CustomSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-customspan)
###### 2.5.4.3.140. [OH_ArkUI_TextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-textstyle)
###### 2.5.4.3.141. [OH_ArkUI_ParagraphStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-paragraphstyle)
###### 2.5.4.3.142. [OH_ArkUI_GestureStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-gesturestyle)
###### 2.5.4.3.143. [OH_ArkUI_TextShadowStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-textshadowstyle)
###### 2.5.4.3.144. [OH_ArkUI_DecorationStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-decorationstyle)
###### 2.5.4.3.145. [OH_ArkUI_BaselineOffsetStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-baselineoffsetstyle)
###### 2.5.4.3.146. [OH_ArkUI_LetterSpacingStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-letterspacingstyle)
###### 2.5.4.3.147. [OH_ArkUI_LineHeightStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-lineheightstyle)
###### 2.5.4.3.148. [OH_ArkUI_LineSpacingStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-linespacingstyle)
###### 2.5.4.3.149. [OH_ArkUI_UrlStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-urlstyle)
###### 2.5.4.3.150. [OH_ArkUI_BackgroundColorStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-backgroundcolorstyle)
###### 2.5.4.3.151. [OH_ArkUI_UserDataSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-userdataspan)
###### 2.5.4.3.152. [OH_ArkUI_LeadingMarginSpanDrawInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo)
###### 2.5.4.3.153. [ArkUI_TextLayoutManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textlayoutmanager)
###### 2.5.4.3.154. [ArkUI_TextMarqueeOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textmarqueeoptions)
###### 2.5.4.3.155. [ArkUI_UIInputEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-eventmodule-arkui-uiinputevent)
###### 2.5.4.3.156. [ArkUI_ShowCounterConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textshowcounterconfig)
###### 2.5.4.3.157. [ArkUI_TextContentBaseController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textcontentbasecontroller)
###### 2.5.4.3.158. [PictureInPicture_PipConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pictureinpicture-pipconfig)
###### 2.5.4.3.159. [WindowManager_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager-rect)
###### 2.5.4.3.160. [OH_PixelmapNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-struct)
###### 2.5.4.3.161. [WindowManager_WindowProperties](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager-windowproperties)
###### 2.5.4.3.162. [WindowManager_AvoidArea](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager-avoidarea)
###### 2.5.4.3.163. [WindowManager_MainWindowInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager-windowmanager-mainwindowinfo)
###### 2.5.4.3.164. [WindowManager_WindowSnapshotConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager-windowmanager-windowsnapshotconfig)
###### 2.5.4.3.165. [OH_WindowManager_FrameMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager-oh-windowmanager-framemetrics)
###### 2.5.4.3.166. [OH_WindowManager_DensityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager-oh-windowmanager-densityinfo)
###### 2.5.4.3.167. [NativeDisplayManager_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-rect)
###### 2.5.4.3.168. [NativeDisplayManager_WaterfallDisplayAreaRects](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-waterfalldisplayarearects)
###### 2.5.4.3.169. [NativeDisplayManager_CutoutInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-cutoutinfo)
###### 2.5.4.3.170. [NativeDisplayManager_DisplayHdrFormat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displayhdrformat)
###### 2.5.4.3.171. [NativeDisplayManager_DisplayColorSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displaycolorspace)
###### 2.5.4.3.172. [NativeDisplayManager_DisplayInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displayinfo)
###### 2.5.4.3.173. [NativeDisplayManager_DisplaysInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displaysinfo)
###### 2.5.4.3.174. [ArkUI_CircleShapeOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-circleshapeoption)
###### 2.5.4.3.175. [ArkUI_ColorAnimatablePropertyHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-coloranimatablepropertyhandle)
###### 2.5.4.3.176. [ArkUI_ColorPropertyHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-colorpropertyhandle)
###### 2.5.4.3.177. [ArkUI_CommandPathOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-commandpathoption)
###### 2.5.4.3.178. [ArkUI_FloatAnimatablePropertyHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-floatanimatablepropertyhandle)
###### 2.5.4.3.179. [ArkUI_FloatPropertyHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-floatpropertyhandle)
###### 2.5.4.3.180. [ArkUI_NodeBorderColorOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodebordercoloroption)
###### 2.5.4.3.181. [ArkUI_NodeBorderRadiusOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodeborderradiusoption)
###### 2.5.4.3.182. [ArkUI_NodeBorderStyleOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodeborderstyleoption)
###### 2.5.4.3.183. [ArkUI_NodeBorderWidthOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodeborderwidthoption)
###### 2.5.4.3.184. [ArkUI_RectShapeOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-rectshapeoption)
###### 2.5.4.3.185. [ArkUI_RenderContentModifierHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-rendercontentmodifierhandle)
###### 2.5.4.3.186. [ArkUI_RenderNodeClipOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-rendernodeclipoption)
###### 2.5.4.3.187. [ArkUI_RenderNodeHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-rendernodehandle)
###### 2.5.4.3.188. [ArkUI_RenderNodeMaskOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-rendernodemaskoption)
###### 2.5.4.3.189. [ArkUI_RoundRectShapeOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-roundrectshapeoption)
###### 2.5.4.3.190. [ArkUI_Vector2AnimatablePropertyHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-vector2animatablepropertyhandle)
###### 2.5.4.3.191. [ArkUI_Vector2PropertyHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-vector2propertyhandle)
###### 2.5.4.3.192. [ArkUI_ContentTransitionEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-contenttransitioneffect)
###### 2.5.4.3.193. [ArkUI_CoastingAxisEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-coastingaxisevent)
###### 2.5.4.3.194. [ArkUI_GridItemRect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-griditemrect)
###### 2.5.4.3.195. [ArkUI_GridItemSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-griditemsize)
###### 2.5.4.3.196. [ArkUI_GridLayoutOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-gridlayoutoptions)
###### 2.5.4.3.197. [ArkUI_TouchTestInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-touchtestinfo)
###### 2.5.4.3.198. [ArkUI_TouchTestInfoItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-touchtestinfoitem)
###### 2.5.4.3.199. [ArkUI_TouchTestInfoItem*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-touchtestinfoitemhandle)
###### 2.5.4.3.200. [ArkUI_TouchTestInfoItemHandle*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-touchtestinfoitemhandlearray)
###### 2.5.4.3.201. [ArkUI_TextMenuItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textmenuitem)
###### 2.5.4.3.202. [ArkUI_TextMenuItemArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textmenuitemarray)
###### 2.5.4.3.203. [ArkUI_TextEditMenuOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-texteditmenuoptions)
###### 2.5.4.3.204. [ArkUI_TextSelectionMenuOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textselectionmenuoptions)
###### 2.5.4.3.205. [ArkUI_SelectedDragPreviewStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textselecteddragpreviewstyle)
###### 2.5.4.3.206. [ArkUI_PickerIndicatorBackground](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-pickerindicatorbackground)
###### 2.5.4.3.207. [ArkUI_PickerIndicatorDivider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-pickerindicatordivider)
###### 2.5.4.3.208. [ArkUI_PickerIndicatorStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-pickerindicatorstyle)
###### 2.5.4.3.209. [OH_ArkUI_DecorationStyleOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-decorationstyleoptions)
###### 2.5.4.3.210. [OH_ArkUI_TextDataDetectorConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-textdatadetectorconfig)
###### 2.5.4.3.211. [OH_ArkUI_TextEditorSelectionMenuOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-texteditorselectionmenuoptions)
###### 2.5.4.3.212. [OH_ArkUI_TextEditorPlaceholderOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-texteditorplaceholderoptions)
###### 2.5.4.3.213. [OH_ArkUI_TextEditorStyledStringController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-texteditorstyledstringcontroller)
###### 2.5.4.3.214. [OH_ArkUI_TextEditorParagraphStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-texteditorparagraphstyle)
###### 2.5.4.3.215. [OH_ArkUI_ShadowOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-shadowoptions)
###### 2.5.4.3.216. [OH_ArkUI_TextEditorTextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-texteditortextstyle)
###### 2.5.4.3.217. [OH_ArkUI_TextController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-textcontroller)
#### 2.5.5. 错误码

##### 2.5.5.1. UI界面

###### 2.5.5.1.1. [接口调用异常错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-internal)
###### 2.5.5.1.2. [弹窗错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-promptaction)
###### 2.5.5.1.3. [页面路由错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-router)
###### 2.5.5.1.4. [拖拽事件错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-drag-event)
###### 2.5.5.1.5. [图像AI分析错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-image-analyzer)
###### 2.5.5.1.6. [焦点错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-focus)
###### 2.5.5.1.7. [系统资源错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-system-resource)
###### 2.5.5.1.8. [附属节点错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-adopt)
###### 2.5.5.1.9. [半模态错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bindsheet)
###### 2.5.5.1.10. [滚动类组件错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-scroll)
###### 2.5.5.1.11. [截图错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-snapshot)
###### 2.5.5.1.12. [属性字符串错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-styled-string)
###### 2.5.5.1.13. [UI上下文错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uicontext)
###### 2.5.5.1.14. [注册节点渲染状态监听错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-node-render-monitor)
###### 2.5.5.1.15. [交互事件错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-event)
###### 2.5.5.1.16. [Canvas组件错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-canvas)
###### 2.5.5.1.17. [自定义节点错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-node)
###### 2.5.5.1.18. [动态属性设置错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-attributemodifier)
###### 2.5.5.1.19. [逻辑组件错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rendering-control)
###### 2.5.5.1.20. [UIExtension错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uiextension)
###### 2.5.5.1.21. [用户界面外观服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uiappearance)
###### 2.5.5.1.22. [NodeAdapter错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-nodeadapter)
###### 2.5.5.1.23. [XComponent组件错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-xcomponent)
###### 2.5.5.1.24. [Video组件错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-video)
###### 2.5.5.1.25. [状态管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-statemanagement)
###### 2.5.5.1.26. [渲染节点错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-node-render)
###### 2.5.5.1.27. [DrawableDescriptor错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-drawable-descriptor)
###### 2.5.5.1.28. [环境变量错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-env)
###### 2.5.5.1.29. [反色能力错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-force-dark)
##### 2.5.5.2. 图形图像

###### 2.5.5.2.1. [屏幕错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-display)
###### 2.5.5.2.2. [窗口错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-window)
##### 2.5.5.3. UI编译

###### 2.5.5.3.1. [编译错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_ark_ui_compile)
### 2.6. ArkWeb（方舟Web）

#### 2.6.1. ArkTS API

##### 2.6.1.1. @ohos.web.webview (Webview)

###### 2.6.1.1.1. [模块描述](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview)
###### 2.6.1.1.2. [Functions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-f)
###### 2.6.1.1.3. [Class (AdsBlockManager)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-adsblockmanager)
###### 2.6.1.1.4. [Class (BackForwardCacheOptions)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-backforwardcacheoptions)
###### 2.6.1.1.5. [Class (BackForwardCacheSupportedFeatures)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-backforwardcachesupportedfeatures)
###### 2.6.1.1.6. [Class (GeolocationPermissions)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-geolocationpermissions)
###### 2.6.1.1.7. [Class (JsMessageExt)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-jsmessageext)
###### 2.6.1.1.8. [Class (MediaSourceInfo)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-mediasourceinfo)
###### 2.6.1.1.9. [Class (NativeMediaPlayerSurfaceInfo)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-nativemediaplayersurfaceinfo)
###### 2.6.1.1.10. [Class (PdfData)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-pdfdata)
###### 2.6.1.1.11. [Class (ProxyConfig)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-proxyconfig)
###### 2.6.1.1.12. [Class (PrefetchOptions)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-prefetchoptions)
###### 2.6.1.1.13. [Class (ProxyController)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-proxycontroller)
###### 2.6.1.1.14. [Class (ProxyRule)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-proxyrule)
###### 2.6.1.1.15. [Class (SecurityParams)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-securityparams)
###### 2.6.1.1.16. [Class (WebviewController)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller)
###### 2.6.1.1.17. [Class (WebCookieManager)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webcookiemanager)
###### 2.6.1.1.18. [Class (WebDataBase)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webdatabase)
###### 2.6.1.1.19. [Class (WebDownloadDelegate)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webdownloaddelegate)
###### 2.6.1.1.20. [Class (WebDownloadItem)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webdownloaditem)
###### 2.6.1.1.21. [Class (WebDownloadManager)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webdownloadmanager)
###### 2.6.1.1.22. [Class (WebHttpBodyStream)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webhttpbodystream)
###### 2.6.1.1.23. [Class (WebMessageExt)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webmessageext)
###### 2.6.1.1.24. [Class (WebResourceHandler)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webresourcehandler)
###### 2.6.1.1.25. [Class (WebSchemeHandler)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandler)
###### 2.6.1.1.26. [Class (WebSchemeHandlerRequest)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandlerrequest)
###### 2.6.1.1.27. [Class (WebSchemeHandlerResponse)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandlerresponse)
###### 2.6.1.1.28. [Class (WebStorage)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webstorage)
###### 2.6.1.1.29. [Class (UserAgentBrandVersion)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-useragentbrandversion)
###### 2.6.1.1.30. [Class (UserAgentMetadata)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-useragentmetadata)
###### 2.6.1.1.31. [Class (VerifyPinHandler)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-verifypinhandler)
###### 2.6.1.1.32. [Interface (BackForwardList)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-backforwardlist)
###### 2.6.1.1.33. [Interface (NativeMediaPlayerBridge)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-nativemediaplayerbridge)
###### 2.6.1.1.34. [Interface (NativeMediaPlayerHandler)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-nativemediaplayerhandler)
###### 2.6.1.1.35. [Interface (WebMessagePort)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webmessageport)
###### 2.6.1.1.36. [Interfaces (其他)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-i)
###### 2.6.1.1.37. [Enums](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-e)
###### 2.6.1.1.38. [Types](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-t)
##### 2.6.1.2. [@ohos.web.netErrorList (ArkWeb网络协议栈错误列表)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-neterrorlist)
##### 2.6.1.3. [@ohos.web.WebNativeMessagingExtensionAbility (Web Native Messaging Extension Ability)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-web-webnativemessagingextensionability)
##### 2.6.1.4. [@ohos.web.WebNativeMessagingExtensionContext (Web Native Messaging Extension Context)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-web-webnativemessagingextensioncontext)
##### 2.6.1.5. [@ohos.web.webNativeMessagingExtensionManager (Web Native Messaging Extension Manager)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-web-webnativemessagingextensionmanager)
#### 2.6.2. ArkTS 组件

##### 2.6.2.1. Web

###### 2.6.2.1.1. [组件描述](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web)
###### 2.6.2.1.2. [属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-attributes)
###### 2.6.2.1.3. [事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events)
###### 2.6.2.1.4. [Class (ClientAuthenticationHandler)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-clientauthenticationhandler)
###### 2.6.2.1.5. [Class (ConsoleMessage)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-consolemessage)
###### 2.6.2.1.6. [Class (ControllerHandler)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-controllerhandler)
###### 2.6.2.1.7. [Class (DataResubmissionHandler)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-dataresubmissionhandler)
###### 2.6.2.1.8. [Class (EventResult)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-eventresult)
###### 2.6.2.1.9. [Class (FileSelectorParam)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-fileselectorparam)
###### 2.6.2.1.10. [Class (FileSelectorResult)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-fileselectorresult)
###### 2.6.2.1.11. [Class (FullScreenExitHandler)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-fullscreenexithandler)
###### 2.6.2.1.12. [Class (HttpAuthHandler)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-httpauthhandler)
###### 2.6.2.1.13. [Class (JsGeolocation)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-jsgeolocation)
###### 2.6.2.1.14. [Class (JsResult)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-jsresult)
###### 2.6.2.1.15. [Class (PermissionRequest)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-permissionrequest)
###### 2.6.2.1.16. [Class (ScreenCaptureHandler)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-screencapturehandler)
###### 2.6.2.1.17. [Class (SslErrorHandler)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-sslerrorhandler)
###### 2.6.2.1.18. [Class (WebContextMenuParam)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webcontextmenuparam)
###### 2.6.2.1.19. [Class (WebContextMenuResult)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webcontextmenuresult)
###### 2.6.2.1.20. [Class (WebCookie)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webcookie)
###### 2.6.2.1.21. [Class (WebKeyboardController)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webkeyboardcontroller)
###### 2.6.2.1.22. [Class (WebResourceError)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webresourceerror)
###### 2.6.2.1.23. [Class (WebResourceRequest)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webresourcerequest)
###### 2.6.2.1.24. [Class (WebResourceResponse)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webresourceresponse)
###### 2.6.2.1.25. [Interfaces（其他）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-i)
###### 2.6.2.1.26. [Enums](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-e)
###### 2.6.2.1.27. [Types](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-t)
###### 2.6.2.1.28. [Class (WebController)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webcontroller)
#### 2.6.3. C API

##### 2.6.3.1. 模块

###### 2.6.3.1.1. [Web](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web)
##### 2.6.3.2. 头文件

###### 2.6.3.2.1. [arkweb_error_code.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-error-code-h)
###### 2.6.3.2.2. [arkweb_interface.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-interface-h)
###### 2.6.3.2.3. [arkweb_net_error_list.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-net-error-list-h)
###### 2.6.3.2.4. [arkweb_scheme_handler.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-scheme-handler-h)
###### 2.6.3.2.5. [arkweb_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-type-h)
###### 2.6.3.2.6. [native_interface_arkweb.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-arkweb-h)
##### 2.6.3.3. 结构体

###### 2.6.3.3.1. [ArkWeb_AnyNativeAPI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-anynativeapi)
###### 2.6.3.3.2. [ArkWeb_BlanklessInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-blanklessinfo)
###### 2.6.3.3.3. [ArkWeb_SchemeHandler_](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-schemehandler)
###### 2.6.3.3.4. [ArkWeb_ResourceHandler_](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-resourcehandler)
###### 2.6.3.3.5. [ArkWeb_Response_](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-response)
###### 2.6.3.3.6. [ArkWeb_ResourceRequest_](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-resourcerequest)
###### 2.6.3.3.7. [ArkWeb_RequestHeaderList_](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-requestheaderlist)
###### 2.6.3.3.8. [ArkWeb_HttpBodyStream_](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-httpbodystream)
###### 2.6.3.3.9. [ArkWeb_JavaScriptBridgeData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-javascriptbridgedata)
###### 2.6.3.3.10. [ArkWeb_WebMessage*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-webmessage8h)
###### 2.6.3.3.11. [ArkWeb_JavaScriptValue*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-javascriptvalue8h)
###### 2.6.3.3.12. [ArkWeb_WebMessagePort*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-webmessageport8h)
###### 2.6.3.3.13. [ArkWeb_JavaScriptObject](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-javascriptobject)
###### 2.6.3.3.14. [ArkWeb_ProxyMethod](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-proxymethod)
###### 2.6.3.3.15. [ArkWeb_ProxyMethodWithResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-proxymethodwithresult)
###### 2.6.3.3.16. [ArkWeb_ProxyObject](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-proxyobject)
###### 2.6.3.3.17. [ArkWeb_ProxyObjectWithResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-proxyobjectwithresult)
###### 2.6.3.3.18. [ArkWeb_ControllerAPI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-controllerapi)
###### 2.6.3.3.19. [ArkWeb_ComponentAPI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-componentapi)
###### 2.6.3.3.20. [ArkWeb_WebMessagePortAPI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-webmessageportapi)
###### 2.6.3.3.21. [ArkWeb_WebMessageAPI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-webmessageapi)
###### 2.6.3.3.22. [ArkWeb_CookieManagerAPI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-cookiemanagerapi)
###### 2.6.3.3.23. [ArkWeb_JavaScriptValueAPI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-javascriptvalueapi)
#### 2.6.4. 错误码

##### 2.6.4.1. [Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)
### 2.7. Background Tasks Kit（后台任务开发服务）

#### 2.7.1. ArkTS API

##### 2.7.1.1. [@ohos.reminderAgentManager (后台代理提醒)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager)
##### 2.7.1.2. [@ohos.resourceschedule.backgroundTaskManager (后台任务管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager)
##### 2.7.1.3. [@ohos.resourceschedule.workScheduler (延迟任务调度)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-workscheduler)
##### 2.7.1.4. [@ohos.WorkSchedulerExtensionAbility (延迟任务调度回调)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-workschedulerextensionability)
##### 2.7.1.5. [@ohos.resourceschedule.backgroundProcessManager (后台子进程管控)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-backgroundprocessmanager)
##### 2.7.1.6. application

###### 2.7.1.6.1. [WorkSchedulerExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-workschedulerextensioncontext)
##### 2.7.1.7. 已停止维护的接口

###### 2.7.1.7.1. [@ohos.backgroundTaskManager (后台任务管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-backgroundtaskmanager)
###### 2.7.1.7.2. [@ohos.bundleState (设备使用信息统计)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-deviceusagestatistics)
###### 2.7.1.7.3. [@ohos.reminderAgent (后台代理提醒)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagent)
#### 2.7.2. C API

##### 2.7.2.1. 模块

###### 2.7.2.1.1. [BackgroundProcessManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-backgroundprocessmanager)
###### 2.7.2.1.2. [TransientTask](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-transienttask)
##### 2.7.2.2. 头文件

###### 2.7.2.2.1. [background_process_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-background-process-manager-h)
###### 2.7.2.2.2. [transient_task_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-transient-task-api-h)
###### 2.7.2.2.3. [transient_task_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-transient-task-type-h)
##### 2.7.2.3. 结构体

###### 2.7.2.3.1. [TransientTask_DelaySuspendInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-transienttask-transienttask-delaysuspendinfo)
###### 2.7.2.3.2. [TransientTask_TransientTaskInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-transienttask-transienttask-transienttaskinfo)
#### 2.7.3. 错误码

##### 2.7.3.1. [backgroundTaskManager错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-backgroundtaskmgr)
##### 2.7.3.2. [backgroundProcessManager错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-backgroundprocessmanager)
##### 2.7.3.3. [reminderAgentManager错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-reminderagentmanager)
##### 2.7.3.4. [workScheduler错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-workscheduler)
### 2.8. Content Embed Kit（内容嵌入服务）

#### 2.8.1. C API

##### 2.8.1.1. 模块

###### 2.8.1.1.1. [ContentEmbed](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed)
##### 2.8.1.2. 头文件

###### 2.8.1.2.1. [content_embed_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-common-h)
###### 2.8.1.2.2. [content_embed_document.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-document-h)
###### 2.8.1.2.3. [content_embed_extension.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-extension-h)
###### 2.8.1.2.4. [content_embed_proxy.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-proxy-h)
##### 2.8.1.3. 结构体

###### 2.8.1.3.1. [ContentEmbed_Document](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-document)
###### 2.8.1.3.2. [ContentEmbed_Storage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-storage)
###### 2.8.1.3.3. [ContentEmbed_StorageElement](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-storageelement)
###### 2.8.1.3.4. [ContentEmbed_StorageElements](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-storageelements)
###### 2.8.1.3.5. [ContentEmbed_Stream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-stream)
###### 2.8.1.3.6. [ContentEmbed_ExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-extensioncontext)
###### 2.8.1.3.7. [ContentEmbed_ExtensionContext*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-extensioncontext8h)
###### 2.8.1.3.8. [ContentEmbed_ExtensionInstance](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-extensioninstance)
###### 2.8.1.3.9. [ContentEmbed_ExtensionInstance*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-extensioninstance8h)
###### 2.8.1.3.10. [ContentEmbed_Object](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-object)
###### 2.8.1.3.11. [ContentEmbed_Object*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-object8h)
###### 2.8.1.3.12. [ContentEmbed_Info](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-info)
###### 2.8.1.3.13. [ContentEmbed_Format](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-format)
###### 2.8.1.3.14. [ContentEmbed_ExtensionProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-extensionproxy)
###### 2.8.1.3.15. [ContentEmbed_Capability](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-capability)
### 2.9. Core File Kit（文件基础服务）

#### 2.9.1. ArkTS API

##### 2.9.1.1. [@ohos.application.BackupExtensionAbility (备份恢复扩展能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-backupextensionability)
##### 2.9.1.2. [@ohos.file.cloudSync (端云同步能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-cloudsync)
##### 2.9.1.3. [@ohos.file.cloudSyncManager (端云同步管理能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-cloudsyncmanager)
##### 2.9.1.4. [@ohos.file.environment (目录环境能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-environment)
##### 2.9.1.5. [@ohos.file.fileuri (文件URI)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fileuri)
##### 2.9.1.6. [@ohos.file.fs (文件管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs)
##### 2.9.1.7. [@ohos.file.hash (文件哈希处理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-hash)
##### 2.9.1.8. [@ohos.file.picker (选择器)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-picker)
##### 2.9.1.9. [@ohos.file.securityLabel (数据标签)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-securitylabel)
##### 2.9.1.10. [@ohos.file.statvfs (文件系统空间统计)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-statvfs)
##### 2.9.1.11. [@ohos.file.storageStatistics (应用空间统计)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-storage-statistics)
##### 2.9.1.12. [@ohos.fileshare (文件分享)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-fileshare)
##### 2.9.1.13. [@ohos.file.BackupExtensionContext (备份恢复扩展能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-backupextensioncontext)
##### 2.9.1.14. 已停止维护的接口

###### 2.9.1.14.1. [@ohos.document (文件交互)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-document)
###### 2.9.1.14.2. [@ohos.fileio (文件管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-fileio)
###### 2.9.1.14.3. [@ohos.statfs (statfs)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-statfs)
###### 2.9.1.14.4. [@system.file (文件存储)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-file)
#### 2.9.2. C API

##### 2.9.2.1. 模块

###### 2.9.2.1.1. [Environment](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-environment)
###### 2.9.2.1.2. [FileIO](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fileio)
###### 2.9.2.1.3. [fileShare](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fileshare)
###### 2.9.2.1.4. [fileUri](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fileuri)
###### 2.9.2.1.5. [CloudDisk](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk)
##### 2.9.2.2. 头文件

###### 2.9.2.2.1. [oh_environment.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-environment-h)
###### 2.9.2.2.2. [error_code.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-error-code-h)
###### 2.9.2.2.3. [oh_fileio.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-fileio-h)
###### 2.9.2.2.4. [oh_file_share.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-file-share-h)
###### 2.9.2.2.5. [oh_file_uri.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-file-uri-h)
###### 2.9.2.2.6. [oh_cloud_disk_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-cloud-disk-manager-h)
###### 2.9.2.2.7. [cloud_disk_error_code.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cloud-disk-error-code-h)
##### 2.9.2.3. 结构体

###### 2.9.2.3.1. [FileShare_PolicyErrorResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fileshare-fileshare-policyerrorresult)
###### 2.9.2.3.2. [FileShare_PolicyInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fileshare-fileshare-policyinfo)
###### 2.9.2.3.3. [CloudDisk_ChangeData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-changedata)
###### 2.9.2.3.4. [CloudDisk_ChangesResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-changesresult)
###### 2.9.2.3.5. [CloudDisk_DisplayNameInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-displaynameinfo)
###### 2.9.2.3.6. [CloudDisk_FailedList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-failedlist)
###### 2.9.2.3.7. [CloudDisk_FileSyncState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-filesyncstate)
###### 2.9.2.3.8. [CloudDisk_PathInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-pathinfo)
###### 2.9.2.3.9. [CloudDisk_ResultList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-resultlist)
###### 2.9.2.3.10. [CloudDisk_SyncFolder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-syncfolder)
#### 2.9.3. 错误码

##### 2.9.3.1. [文件管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement)
### 2.10. Data Augmentation Kit（数据增强服务）

#### 2.10.1. ArkTS API

##### 2.10.1.1. [rag（检索增强生成）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-rag-api)
##### 2.10.1.2. [retrieval（智慧化数据平台）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-retrieval-api)
##### 2.10.1.3. [knowledgeProcessor（知识加工）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-knowledgeprocessor-api)
##### 2.10.1.4. [localChatModel（端侧问答模型）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-localchatmodel-api)
##### 2.10.1.5. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-dataaugmentation)
#### 2.10.2. C API

##### 2.10.2.1. 模块

###### 2.10.2.1.1. [AIP](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-aip)
###### 2.10.2.1.2. [Retrieval](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval)
##### 2.10.2.2. 头文件

###### 2.10.2.2.1. [aip_error_code.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-aip-error-code)
###### 2.10.2.2.2. [aip_retrieval.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-aip-retrieval)
###### 2.10.2.2.3. [aip_retrieval_condition.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-aip-retrieval-condition)
###### 2.10.2.2.4. [aip_retrieval_condition_vector.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-aip-retrieval-condition-vector)
###### 2.10.2.2.5. [aip_retrieval_query.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-aip-retrieval-query)
###### 2.10.2.2.6. [aip_retrieval_record.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-aip-retrieval-record)
### 2.11. Form Kit（卡片开发服务）

#### 2.11.1. ArkTS API

##### 2.11.1.1. [@ohos.app.form.formBindingData (卡片数据绑定类)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-formbindingdata)
##### 2.11.1.2. [@ohos.app.form.FormExtensionAbility (FormExtensionAbility)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-formextensionability)
##### 2.11.1.3. [@ohos.app.form.formInfo (formInfo)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-forminfo)
##### 2.11.1.4. [@ohos.app.form.formProvider (formProvider)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-formprovider)
##### 2.11.1.5. [@ohos.app.form.FormEditExtensionAbility (FormEditExtensionAbility)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-formeditextensionability)
##### 2.11.1.6. [@ohos.app.form.LiveFormExtensionAbility (LiveFormExtensionAbility)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-liveformextensionability)
##### 2.11.1.7. application

###### 2.11.1.7.1. [FormExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-formextensioncontext)
###### 2.11.1.7.2. [FormEditExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-formeditextensioncontext)
###### 2.11.1.7.3. [LiveFormExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-liveformextensioncontext)
#### 2.11.2. 已停止维护的接口

##### 2.11.2.1. [@ohos.application.formBindingData (卡片数据绑定类)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-formbindingdata)
##### 2.11.2.2. [@ohos.application.formError (formError)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-formerror)
##### 2.11.2.3. [@ohos.application.formInfo (formInfo)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-forminfo)
##### 2.11.2.4. [@ohos.application.formProvider (formProvider)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-formprovider)
#### 2.11.3. 错误码

##### 2.11.3.1. [卡片错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-form)
### 2.12. IME Kit（输入法开发服务）

#### 2.12.1. ArkTS API

##### 2.12.1.1. [@ohos.InputMethodExtensionAbility (InputMethodExtensionAbility)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-extension-ability)
##### 2.12.1.2. [@ohos.InputMethodExtensionContext (InputMethodExtensionContext)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-extension-context)
##### 2.12.1.3. [@ohos.inputMethod.Panel (输入法面板)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-panel)
##### 2.12.1.4. [@ohos.InputMethodSubtype (输入法子类型)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-subtype)
##### 2.12.1.5. [@ohos.inputMethod (输入法框架)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod)
##### 2.12.1.6. [@ohos.inputMethodEngine (输入法服务)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethodengine)
##### 2.12.1.7. [@ohos.inputMethodList (输入法切换列表控件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethodlist)
##### 2.12.1.8. [@ohos.inputMethod.ExtraConfig (输入法扩展信息)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-extraconfig)
#### 2.12.2. C API

##### 2.12.2.1. 模块

###### 2.12.2.1.1. [InputMethod](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod)
##### 2.12.2.2. 头文件

###### 2.12.2.2.1. [inputmethod_attach_options_capi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-attach-options-capi-h)
###### 2.12.2.2.2. [inputmethod_controller_capi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-controller-capi-h)
###### 2.12.2.2.3. [inputmethod_cursor_info_capi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-cursor-info-capi-h)
###### 2.12.2.2.4. [inputmethod_inputmethod_proxy_capi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-inputmethod-proxy-capi-h)
###### 2.12.2.2.5. [inputmethod_private_command_capi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-private-command-capi-h)
###### 2.12.2.2.6. [inputmethod_text_avoid_info_capi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-text-avoid-info-capi-h)
###### 2.12.2.2.7. [inputmethod_text_config_capi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-text-config-capi-h)
###### 2.12.2.2.8. [inputmethod_text_editor_proxy_capi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-text-editor-proxy-capi-h)
###### 2.12.2.2.9. [inputmethod_types_capi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-types-capi-h)
##### 2.12.2.3. 结构体

###### 2.12.2.3.1. [InputMethod_AttachOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-inputmethod-attachoptions)
###### 2.12.2.3.2. [InputMethod_CursorInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-inputmethod-cursorinfo)
###### 2.12.2.3.3. [InputMethod_InputMethodProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-inputmethod-inputmethodproxy)
###### 2.12.2.3.4. [InputMethod_PrivateCommand](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-inputmethod-privatecommand)
###### 2.12.2.3.5. [InputMethod_TextAvoidInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-inputmethod-textavoidinfo)
###### 2.12.2.3.6. [InputMethod_TextConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-inputmethod-textconfig)
###### 2.12.2.3.7. [InputMethod_TextEditorProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-inputmethod-texteditorproxy)
#### 2.12.3. 错误码

##### 2.12.3.1. [输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)
### 2.13. IPC Kit（进程间通信服务）

#### 2.13.1. ArkTS API

##### 2.13.1.1. [@ohos.rpc (RPC通信)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-rpc)
#### 2.13.2. C API

##### 2.13.2.1. 模块

###### 2.13.2.1.1. [OHIPCParcel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohipcparcel)
###### 2.13.2.1.2. [OHIPCRemoteObject](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohipcremoteobject)
###### 2.13.2.1.3. [OHIPCSkeleton](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohipcskeleton)
###### 2.13.2.1.4. [OHIPCErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohipcerrorcode)
###### 2.13.2.1.5. [IPCKit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ipckit)
##### 2.13.2.2. 头文件

###### 2.13.2.2.1. [ipc_cparcel.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ipc-cparcel-h)
###### 2.13.2.2.2. [ipc_cremote_object.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ipc-cremote-object-h)
###### 2.13.2.2.3. [ipc_cskeleton.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ipc-cskeleton-h)
###### 2.13.2.2.4. [ipc_error_code.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ipc-error-code-h)
###### 2.13.2.2.5. [ipc_kit.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ipc-kit-h)
##### 2.13.2.3. 结构体

###### 2.13.2.3.1. [OHIPCParcel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohipcparcel-ohipcparcel)
###### 2.13.2.3.2. [OH_IPC_MessageOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohipcremoteobject-oh-ipc-messageoption)
###### 2.13.2.3.3. [OHIPCRemoteProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohipcparcel-ohipcremoteproxy)
###### 2.13.2.3.4. [OHIPCRemoteStub](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohipcparcel-ohipcremotestub)
###### 2.13.2.3.5. [OHIPCDeathRecipient](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohipcremoteobject-ohipcdeathrecipient)
#### 2.13.3. 错误码

##### 2.13.3.1. [RPC错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)
### 2.14. Localization Kit（本地化开发服务）

#### 2.14.1. ArkTS API

##### 2.14.1.1. [@ohos.i18n (国际化-I18n)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-i18n)
##### 2.14.1.2. [@ohos.intl (国际化-Intl)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-intl)
##### 2.14.1.3. [@ohos.resourceManager (资源管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager)
##### 2.14.1.4. [@ohos.sendableResourceManager (资源管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sendable-resource-manager)
##### 2.14.1.5. global

###### 2.14.1.5.1. [RawFileDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-rawfiledescriptor)
###### 2.14.1.5.2. [Resource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource)
###### 2.14.1.5.3. [SendableResource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sendableresource)
#### 2.14.2. C API

##### 2.14.2.1. 模块

###### 2.14.2.1.1. [rawfile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile)
###### 2.14.2.1.2. [resourcemanager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-resourcemanager)
###### 2.14.2.1.3. [i18n](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n)
##### 2.14.2.2. 头文件

###### 2.14.2.2.1. [ohresmgr.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohresmgr-h)
###### 2.14.2.2.2. [raw_dir.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-raw-dir-h)
###### 2.14.2.2.3. [raw_file.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-raw-file-h)
###### 2.14.2.2.4. [raw_file_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-raw-file-manager-h)
###### 2.14.2.2.5. [resmgr_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-resmgr-common-h)
###### 2.14.2.2.6. [timezone.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-timezone-h)
###### 2.14.2.2.7. [errorcode.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-errorcode-h)
##### 2.14.2.3. 结构体

###### 2.14.2.3.1. [RawDir](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawdir)
###### 2.14.2.3.2. [RawFileDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawfiledescriptor)
###### 2.14.2.3.3. [RawFileDescriptor64](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawfiledescriptor64)
###### 2.14.2.3.4. [RawFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawfile)
###### 2.14.2.3.5. [RawFile64](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawfile64)
###### 2.14.2.3.6. [NativeResourceManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-nativeresourcemanager)
###### 2.14.2.3.7. [ResourceManager_Configuration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-resourcemanager-resourcemanager-configuration)
###### 2.14.2.3.8. [DateTimeRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-datetimerule)
###### 2.14.2.3.9. [InitialTimeZoneRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-initialtimezonerule)
###### 2.14.2.3.10. [TimeArrayTimeZoneRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timearraytimezonerule)
###### 2.14.2.3.11. [AnnualTimeZoneRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-annualtimezonerule)
###### 2.14.2.3.12. [TimeZoneRules](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timezonerules)
###### 2.14.2.3.13. [TimeZoneRuleQuery](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timezonerulequery)
#### 2.14.3. 错误码

##### 2.14.3.1. [I18n错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-i18n)
##### 2.14.3.2. [资源管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-resource-manager)
### 2.15. UI Design Kit（UI设计套件）

#### 2.15.1. ArkTS API

##### 2.15.1.1. [hdsDrawable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsdrawable)
##### 2.15.1.2. [symbolRegister](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-symbolregister)
##### 2.15.1.3. [hdsEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdseffect)
##### 2.15.1.4. [hdsMaterial](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsmaterial)
##### 2.15.1.5. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-ui-design)
#### 2.15.2. ArkTS组件

##### 2.15.2.1. [HdsNavigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavigation)
##### 2.15.2.2. [HdsNavDestination](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavdestination)
##### 2.15.2.3. [HdsSideBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdssidebar)
##### 2.15.2.4. [HdsSnackBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdssnackbar)
##### 2.15.2.5. [HdsSideMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdssidemenu)
##### 2.15.2.6. [HdsActionBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsactionbar)
##### 2.15.2.7. [HdsTabs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdstabs)
##### 2.15.2.8. [HdsListItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdslistitem)
##### 2.15.2.9. [HdsListItemCard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdslistitemcard)
##### 2.15.2.10. [HdsVisualComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hds-visual-component)
##### 2.15.2.11. [MultiWindowEntryInAPP](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-multiwindowentryinapp-api)

## 3. 系统

### 3.1. 安全

#### 3.1.1. Asset Store Kit（关键资产存储服务）

##### 3.1.1.1. ArkTS API

###### 3.1.1.1.1. [@ohos.security.asset (关键资产存储服务)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-asset)
##### 3.1.1.2. C API

###### 3.1.1.2.1. 模块

###### 3.1.1.2.1.1. [AssetApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assetapi)
###### 3.1.1.2.1.2. [AssetType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype)
###### 3.1.1.2.2. 头文件

###### 3.1.1.2.2.1. [asset_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-asset-api-h)
###### 3.1.1.2.2.2. [asset_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-asset-type-h)
###### 3.1.1.2.3. 结构体

###### 3.1.1.2.3.1. [Asset_Blob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-blob)
###### 3.1.1.2.3.2. [Asset_Value](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-value)
###### 3.1.1.2.3.3. [Asset_Attr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-attr)
###### 3.1.1.2.3.4. [Asset_Result](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-result)
###### 3.1.1.2.3.5. [Asset_ResultSet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-resultset)
###### 3.1.1.2.3.6. [Asset_SyncResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-syncresult)
##### 3.1.1.3. 错误码

###### 3.1.1.3.1. [关键资产存储服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-asset)
#### 3.1.2. Crypto Architecture Kit（加解密算法框架服务）

##### 3.1.2.1. ArkTS API

###### 3.1.2.1.1. [@ohos.security.cryptoFramework (加解密算法库框架)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework)
###### 3.1.2.1.2. 已停止维护的接口

###### 3.1.2.1.2.1. [@system.cipher (加密算法)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-cipher)
##### 3.1.2.2. C API

###### 3.1.2.2.1. 模块

###### 3.1.2.2.1.1. [CryptoArchitectureKit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoarchitecturekit)
###### 3.1.2.2.1.2. [CryptoAsymCipherApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymcipherapi)
###### 3.1.2.2.1.3. [CryptoAsymKeyApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymkeyapi)
###### 3.1.2.2.1.4. [CryptoCommonApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi)
###### 3.1.2.2.1.5. [CryptoDigestApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptodigestapi)
###### 3.1.2.2.1.6. [CryptoKdfApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptokdfapi)
###### 3.1.2.2.1.7. [CryptoKeyAgreementApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptokeyagreementapi)
###### 3.1.2.2.1.8. [CryptoMacApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptomacapi)
###### 3.1.2.2.1.9. [CryptoRandApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptorandapi)
###### 3.1.2.2.1.10. [CryptoSignatureApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosignatureapi)
###### 3.1.2.2.1.11. [CryptoSymCipherApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosymcipherapi)
###### 3.1.2.2.1.12. [CryptoSymKeyApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosymkeyapi)
###### 3.1.2.2.2. 头文件

###### 3.1.2.2.2.1. [crypto_architecture_kit.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-architecture-kit-h)
###### 3.1.2.2.2.2. [crypto_asym_cipher.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h)
###### 3.1.2.2.2.3. [crypto_asym_key.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h)
###### 3.1.2.2.2.4. [crypto_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h)
###### 3.1.2.2.2.5. [crypto_digest.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-digest-h)
###### 3.1.2.2.2.6. [crypto_kdf.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-kdf-h)
###### 3.1.2.2.2.7. [crypto_key_agreement.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-key-agreement-h)
###### 3.1.2.2.2.8. [crypto_mac.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-mac-h)
###### 3.1.2.2.2.9. [crypto_rand.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-rand-h)
###### 3.1.2.2.2.10. [crypto_signature.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-signature-h)
###### 3.1.2.2.2.11. [crypto_sym_cipher.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h)
###### 3.1.2.2.2.12. [crypto_sym_key.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h)
###### 3.1.2.2.3. 结构体

###### 3.1.2.2.3.1. [Crypto_DataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi-crypto-datablob)
###### 3.1.2.2.3.2. [OH_CryptoAsymCipher](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymcipherapi-oh-cryptoasymcipher)
###### 3.1.2.2.3.3. [OH_CryptoSm2CiphertextSpec](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymcipherapi-oh-cryptosm2ciphertextspec)
###### 3.1.2.2.3.4. [OH_CryptoKeyPair](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymkeyapi-oh-cryptokeypair)
###### 3.1.2.2.3.5. [OH_CryptoPubKey](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymkeyapi-oh-cryptopubkey)
###### 3.1.2.2.3.6. [OH_CryptoPrivKey](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymkeyapi-oh-cryptoprivkey)
###### 3.1.2.2.3.7. [OH_CryptoAsymKeyGenerator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymkeyapi-oh-cryptoasymkeygenerator)
###### 3.1.2.2.3.8. [OH_CryptoPrivKeyEncodingParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymkeyapi-oh-cryptoprivkeyencodingparams)
###### 3.1.2.2.3.9. [OH_CryptoAsymKeySpec](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymkeyapi-oh-cryptoasymkeyspec)
###### 3.1.2.2.3.10. [OH_CryptoAsymKeyGeneratorWithSpec](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymkeyapi-oh-cryptoasymkeygeneratorwithspec)
###### 3.1.2.2.3.11. [OH_CryptoEcPoint](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymkeyapi-oh-cryptoecpoint)
###### 3.1.2.2.3.12. [OH_CryptoDigest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptodigestapi-oh-cryptodigest)
###### 3.1.2.2.3.13. [OH_CryptoKdf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptokdfapi-oh-cryptokdf)
###### 3.1.2.2.3.14. [OH_CryptoKdfParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptokdfapi-oh-cryptokdfparams)
###### 3.1.2.2.3.15. [OH_CryptoKeyAgreement](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptokeyagreementapi-oh-cryptokeyagreement)
###### 3.1.2.2.3.16. [OH_CryptoMac](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptomacapi-oh-cryptomac)
###### 3.1.2.2.3.17. [OH_CryptoRand](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptorandapi-oh-cryptorand)
###### 3.1.2.2.3.18. [OH_CryptoVerify](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosignatureapi-oh-cryptoverify)
###### 3.1.2.2.3.19. [OH_CryptoSign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosignatureapi-oh-cryptosign)
###### 3.1.2.2.3.20. [OH_CryptoEccSignatureSpec](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosignatureapi-oh-cryptoeccsignaturespec)
###### 3.1.2.2.3.21. [OH_CryptoSymCipher](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosymcipherapi-oh-cryptosymcipher)
###### 3.1.2.2.3.22. [OH_CryptoSymCipherParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosymcipherapi-oh-cryptosymcipherparams)
###### 3.1.2.2.3.23. [OH_CryptoSymKey](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosymkeyapi-oh-cryptosymkey)
###### 3.1.2.2.3.24. [OH_CryptoSymKeyGenerator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosymkeyapi-oh-cryptosymkeygenerator)
##### 3.1.2.3. 错误码

###### 3.1.2.3.1. [cryptoFramework错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-crypto-framework)
#### 3.1.3. Data Protection Kit（数据保护服务）

##### 3.1.3.1. ArkTS API

###### 3.1.3.1.1. [@ohos.dlpPermission (数据防泄漏)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-dlppermission)
###### 3.1.3.1.2. [@ohos.security.identifySensitiveContent (识别敏感内容)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-identifysensitivecontent)
##### 3.1.3.2. C API

###### 3.1.3.2.1. 模块

###### 3.1.3.2.1.1. [DlpPermissionApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-dlppermissionapi)
###### 3.1.3.2.2. 头文件

###### 3.1.3.2.2.1. [dlp_permission_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-dlp-permission-api-h)
##### 3.1.3.3. 错误码

###### 3.1.3.3.1. [DLP服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-dlp)
#### 3.1.4. Device Security Kit（设备安全服务）

##### 3.1.4.1. ArkTS API

###### 3.1.4.1.1. [DeviceVerify（应用设备状态检测）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-deviceverify-api)
###### 3.1.4.1.2. [SafetyDetect（安全检测）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-safetydetectenhanced-api)
###### 3.1.4.1.3. [StarShieldConfidentialRiskControlEngine（星盾机密风控引擎）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-riskcontrolengine-api)
###### 3.1.4.1.4. [TrustedAppService（可信应用服务）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-taas-api)
###### 3.1.4.1.5. [BusinessRiskIntelligentDetection（业务风险检测）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-brid-api)
###### 3.1.4.1.6. [SecurityAudit（安全审计）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-securityaudit-api)
###### 3.1.4.1.7. [AntifraudPicker（反诈选择器）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-antifraudpicker-api)
###### 3.1.4.1.8. [TrustedAuthentication（数字盾服务）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-trusted-auth-api)
###### 3.1.4.1.9. [DlpAntiPeep（防窥保护）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-dlpantipeep-api)
###### 3.1.4.1.10. [SuperPrivacyMode（超级隐私模式）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-superprivacymode-api)
###### 3.1.4.1.11. ArkTS API错误码

###### 3.1.4.1.11.1. [DeviceVerify（应用设备状态检测）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicesecurity-deviceverify)
###### 3.1.4.1.11.2. [SafetyDetect（安全检测）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicesecurity-safetydetect)
###### 3.1.4.1.11.3. [StarShieldConfidentialRiskControlEngine（星盾机密风控引擎）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicesecurity-riskcontrolengine)
###### 3.1.4.1.11.4. [TrustedAppService（可信应用服务）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicesecurity-taas)
###### 3.1.4.1.11.5. [BusinessRiskIntelligentDetection（业务风险检测）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicesecurity-brid)
###### 3.1.4.1.11.6. [SecurityAudit（安全审计）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicesecurity-securityaudit)
###### 3.1.4.1.11.7. [AntifraudPicker（反诈选择器）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicesecurity-antifraudpicker)
###### 3.1.4.1.11.8. [TrustedAuthentication （数字盾服务）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicesecurity-trusted-auth)
###### 3.1.4.1.11.9. [DlpAntiPeep（防窥保护）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicesecurity-dlpantipeep)
###### 3.1.4.1.11.10. [SuperPrivacyMode（超级隐私模式）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicesecurity-superprivacy)
##### 3.1.4.2. C API

###### 3.1.4.2.1. 模块

###### 3.1.4.2.1.1. [DeviceSecurityMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-devicesecuritymode)
###### 3.1.4.2.1.2. [SecurityAudit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-securityaudit)
###### 3.1.4.2.1.3. [SecurityAntivirus](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-securityantivirus)
###### 3.1.4.2.2. 头文件

###### 3.1.4.2.2.1. [device_security_mode.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-device-security-mode-8h)
###### 3.1.4.2.2.2. [security_audit.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-security-audit-8h)
###### 3.1.4.2.2.3. [security_antivirus.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-security-antivirus-8h)
###### 3.1.4.2.3. 结构体

###### 3.1.4.2.3.1. [SecurityAudit_Event](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-structs-securityaudit-event)
###### 3.1.4.2.3.2. [SecurityAudit_Filter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-structs-securityaudit-filter)
###### 3.1.4.2.3.3. [SecurityAntivirus_Antivirus](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-structs-securityantivirus)
##### 3.1.4.3. REST API

###### 3.1.4.3.1. [验证deviceToken](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-deviceverify-checkdevicetoken)
###### 3.1.4.3.2. [查询设备标记状态](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-deviceverify-getdevicestatus)
###### 3.1.4.3.3. [更新设备标记状态](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-deviceverify-updatedevicestatus)
###### 3.1.4.3.4. [删除设备标记状态](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-deviceverify-deletedevicestatus)
###### 3.1.4.3.5. [REST API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-restapi-errcode)
#### 3.1.5. Enterprise Data Guard Kit（企业数据保护服务）

##### 3.1.5.1. ArkTS API

###### 3.1.5.1.1. [fileGuard (文件分级管控)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataguard-fileguard)
###### 3.1.5.1.2. [recoveryKey（企业恢复密钥）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataguard-recoverykey)
###### 3.1.5.1.3. [企业数据保护服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-enterprise-dataguard)
#### 3.1.6. Enterprise Threat Protection Kit（企业威胁防护服务）

##### 3.1.6.1. ArkTS API

###### 3.1.6.1.1. [virusRemediation（病毒检测与处置）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/enterprisethreatprotection-virusremediation-interface)
###### 3.1.6.1.2. [ArkTS API 错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-enterprise-threat-protection)
#### 3.1.7. Online Authentication Kit（在线认证服务）

##### 3.1.7.1. ArkTS API

###### 3.1.7.1.1. [FIDO](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/onlineauthentication-fido-api)
###### 3.1.7.1.2. [IFAA](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/onlineauthentication-ifaa-api)
###### 3.1.7.1.3. [SOTER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/onlineauthentication-soter-api)
###### 3.1.7.1.4. [通行密钥](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/onlineauthentication-passkey-api)
###### 3.1.7.1.5. [DID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/onlineauthentication-did-api)
###### 3.1.7.1.6. ArkTS API错误码

###### 3.1.7.1.6.1. [FIDO](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-onlineauthentication-fido)
###### 3.1.7.1.6.2. [IFAA](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-onlineauthentication-ifaa)
###### 3.1.7.1.6.3. [SOTER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-onlineauthentication-soter)
###### 3.1.7.1.6.4. [通行密钥](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-onlineauthentication-passkey)
###### 3.1.7.1.6.5. [DID数字身份服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-onlineauthentication-did)
##### 3.1.7.2. C API

###### 3.1.7.2.1. 模块

###### 3.1.7.2.1.1. [通行密钥](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)
###### 3.1.7.2.2. 头文件

###### 3.1.7.2.2.1. [fido2_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/onlineauthentication_capi_header_fido2)
###### 3.1.7.2.3. 结构体

###### 3.1.7.2.3.1. [AuthenticationExtensionsClientOutputs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_authentication_extensions_client_outputs)
###### 3.1.7.2.3.2. [FIDO2_AttestationFormatsArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___attestation_formats_array)
###### 3.1.7.2.3.3. [FIDO2_AuthenticatorAttestationResponse](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_attestation_response)
###### 3.1.7.2.3.4. [FIDO2_AuthenticatorMetadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_metadata)
###### 3.1.7.2.3.5. [FIDO2_AuthenticatorMetadataArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_metadata_array)
###### 3.1.7.2.3.6. [FIDO2_AuthenticatorResponse](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_response)
###### 3.1.7.2.3.7. [FIDO2_AuthenticatorSelectionCriteria](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_selection_criteria)
###### 3.1.7.2.3.8. [FIDO2_AuthenticatorTransportArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_transport_array)
###### 3.1.7.2.3.9. [FIDO2_Capability](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___capability)
###### 3.1.7.2.3.10. [FIDO2_CapabilityArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___capability_array)
###### 3.1.7.2.3.11. [FIDO2_CredentialCreationOptionArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___credential_creation_option_array)
###### 3.1.7.2.3.12. [FIDO2_CredentialCreationOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___credential_creation_options)
###### 3.1.7.2.3.13. [FIDO2_CredentialRequestOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___credential_request_options)
###### 3.1.7.2.3.14. [FIDO2_PublicKeyAssertionCredential](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_assertion_credential)
###### 3.1.7.2.3.15. [FIDO2_PublicKeyAttestationCredential](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_attestation_credential)
###### 3.1.7.2.3.16. [FIDO2_PublicKeyCredentialCreationOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_creation_options)
###### 3.1.7.2.3.17. [FIDO2_PublicKeyCredentialDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_descriptor)
###### 3.1.7.2.3.18. [FIDO2_PublicKeyCredentialDescriptorArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_descriptor_array)
###### 3.1.7.2.3.19. [FIDO2_PublicKeyCredentialHintArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_hint_array)
###### 3.1.7.2.3.20. [FIDO2_PublicKeyCredentialParameters](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_parameters)
###### 3.1.7.2.3.21. [FIDO2_PublicKeyCredentialRequestOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_request_options)
###### 3.1.7.2.3.22. [FIDO2_PublicKeyCredentialRpEntity](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_rp_entity)
###### 3.1.7.2.3.23. [FIDO2_PublicKeyCredentialUserEntity](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_user_entity)
###### 3.1.7.2.3.24. [FIDO2_TokenBinding](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___token_binding)
###### 3.1.7.2.3.25. [Uint8Buff](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_uint8_buff)
#### 3.1.8. Device Certificate Kit（设备证书服务）

##### 3.1.8.1. ArkTS API

###### 3.1.8.1.1. [@ohos.security.cert (证书模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cert)
###### 3.1.8.1.2. [@ohos.security.certManager (证书管理模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-certmanager)
###### 3.1.8.1.3. [@ohos.security.certManagerDialog (证书管理对话框模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-certmanagerdialog)
##### 3.1.8.2. C API

###### 3.1.8.2.1. 模块

###### 3.1.8.2.1.1. [CertManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-certmanager)
###### 3.1.8.2.1.2. [CertManagerType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-certmanagertype)
###### 3.1.8.2.2. 头文件

###### 3.1.8.2.2.1. [cm_native_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cm-native-api-h)
###### 3.1.8.2.2.2. [cm_native_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cm-native-type-h)
###### 3.1.8.2.3. 结构体

###### 3.1.8.2.3.1. [OH_CM_Blob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-certmanagertype-oh-cm-blob)
###### 3.1.8.2.3.2. [OH_CM_Credential](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-certmanagertype-oh-cm-credential)
###### 3.1.8.2.3.3. [OH_CM_CredentialDetailList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-certmanagertype-oh-cm-credentialdetaillist)
###### 3.1.8.2.3.4. [OH_CM_UkeyInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-certmanagertype-oh-cm-ukeyinfo)
##### 3.1.8.3. 错误码

###### 3.1.8.3.1. [证书错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-cert)
###### 3.1.8.3.2. [证书管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-certmanager)
###### 3.1.8.3.3. [证书管理对话框错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-certmanagerdialog)
#### 3.1.9. Universal Keystore Kit（密钥管理服务）

##### 3.1.9.1. ArkTS API

###### 3.1.9.1.1. [@ohos.security.huks (通用密钥库系统)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks)
###### 3.1.9.1.2. [@ohos.security.huksExternalCrypto (外部密钥管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huksexternalcrypto)
###### 3.1.9.1.3. [@ohos.security.CryptoExtensionAbility (密钥扩展能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoextensionability)
##### 3.1.9.2. C API

###### 3.1.9.2.1. 模块

###### 3.1.9.2.1.1. [HuksExternalCryptoApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-huksexternalcryptoapi)
###### 3.1.9.2.1.2. [HuksExternalCryptoTypeApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-huksexternalcryptotypeapi)
###### 3.1.9.2.1.3. [HuksKeyApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukskeyapi)
###### 3.1.9.2.1.4. [HuksParamSetApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-huksparamsetapi)
###### 3.1.9.2.1.5. [HuksTypeApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi)
###### 3.1.9.2.2. 头文件

###### 3.1.9.2.2.1. [native_huks_external_crypto_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-external-crypto-api-h)
###### 3.1.9.2.2.2. [native_huks_external_crypto_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-external-crypto-type-h)
###### 3.1.9.2.2.3. [native_huks_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-api-h)
###### 3.1.9.2.2.4. [native_huks_param.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-param-h)
###### 3.1.9.2.2.5. [native_huks_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-type-h)
###### 3.1.9.2.3. 结构体

###### 3.1.9.2.3.1. [OH_Huks_ExternalCryptoParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-huksexternalcryptotypeapi-oh-huks-externalcryptoparam)
###### 3.1.9.2.3.2. [OH_Huks_ExternalCryptoParamSet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-huksexternalcryptotypeapi-oh-huks-externalcryptoparamset)
###### 3.1.9.2.3.3. [OH_Huks_Result](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-result)
###### 3.1.9.2.3.4. [OH_Huks_Blob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-blob)
###### 3.1.9.2.3.5. [OH_Huks_Param](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-param)
###### 3.1.9.2.3.6. [OH_Huks_ParamSet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-paramset)
###### 3.1.9.2.3.7. [OH_Huks_CertChain](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-certchain)
###### 3.1.9.2.3.8. [OH_Huks_KeyInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-keyinfo)
###### 3.1.9.2.3.9. [OH_Huks_PubKeyInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-pubkeyinfo)
###### 3.1.9.2.3.10. [OH_Huks_KeyMaterialRsa](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-keymaterialrsa)
###### 3.1.9.2.3.11. [OH_Huks_KeyMaterialEcc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-keymaterialecc)
###### 3.1.9.2.3.12. [OH_Huks_KeyMaterialDsa](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-keymaterialdsa)
###### 3.1.9.2.3.13. [OH_Huks_KeyMaterialDh](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-keymaterialdh)
###### 3.1.9.2.3.14. [OH_Huks_KeyMaterial25519](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-keymaterial25519)
###### 3.1.9.2.3.15. [OH_Huks_KeyAliasSet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-keyaliasset)
##### 3.1.9.3. 错误码

###### 3.1.9.3.1. [HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)
#### 3.1.10. User Authentication Kit（用户认证服务）

##### 3.1.10.1. ArkTS API

###### 3.1.10.1.1. [@ohos.userIAM.userAuth (用户认证)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-useriam-userauth)
##### 3.1.10.2. ArkTS组件

###### 3.1.10.2.1. [@ohos.userIAM.userAuthIcon (嵌入式用户身份认证控件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-useriam-userauthicon)
##### 3.1.10.3. 错误码

###### 3.1.10.3.1. [用户认证错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-useriam)
### 3.2. 网络

#### 3.2.1. Accessory Kit（配件接入服务）

##### 3.2.1.1. ArkTS API

###### 3.2.1.1.1. [accessoryAccessManager（配件接入管理）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/accessory-accessoryaccessmanager)
#### 3.2.2. Connectivity Kit（短距通信服务）

##### 3.2.2.1. ArkTS API

###### 3.2.2.1.1. [@ohos.bluetooth.a2dp (蓝牙a2dp模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-a2dp)
###### 3.2.2.1.2. [@ohos.bluetooth.access (蓝牙access模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-access)
###### 3.2.2.1.3. [@ohos.bluetooth.baseProfile (蓝牙baseProfile模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-baseprofile)
###### 3.2.2.1.4. [@ohos.bluetooth.ble (蓝牙ble模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble)
###### 3.2.2.1.5. [@ohos.bluetooth.connection (蓝牙connection模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection)
###### 3.2.2.1.6. [@ohos.bluetooth.constant (蓝牙constant模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-constant)
###### 3.2.2.1.7. [@ohos.bluetooth.common (蓝牙common模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-common)
###### 3.2.2.1.8. [@ohos.bluetooth.hfp (蓝牙hfp模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-hfp)
###### 3.2.2.1.9. [@ohos.bluetooth.hid (蓝牙hid模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-hid)
###### 3.2.2.1.10. [@ohos.bluetooth.pan (蓝牙pan模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-pan)
###### 3.2.2.1.11. [@ohos.bluetooth.socket (蓝牙socket模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-socket)
###### 3.2.2.1.12. [@ohos.bluetooth.pbap (蓝牙pbap模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-pbap)
###### 3.2.2.1.13. [@ohos.bluetooth.map (蓝牙map模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-map)
###### 3.2.2.1.14. [@ohos.connectedTag (有源标签)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-connectedtag)
###### 3.2.2.1.15. [@ohos.nfc.cardEmulation (标准NFC-cardEmulation)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cardemulation)
###### 3.2.2.1.16. [@ohos.nfc.controller (标准NFC)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-nfccontroller)
###### 3.2.2.1.17. [@ohos.nfc.tag (标准NFC-Tag)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-nfctag)
###### 3.2.2.1.18. [@ohos.secureElement (安全单元的通道管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-secureelement)
###### 3.2.2.1.19. [@ohos.wifiManager (WLAN)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager)
###### 3.2.2.1.20. [@ohos.wifiManagerExt (WLAN扩展接口)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanagerext)
###### 3.2.2.1.21. [@ohos.FusionConnectivity.partnerAgent（设备状态通知模块）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-fusionconnectivity-partneragent)
###### 3.2.2.1.22. [@ohos.FusionConnectivity.PartnerAgentExtensionContext (设备状态通知能力上下文)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-fusionconnectivity-partneragentextensioncontext)
###### 3.2.2.1.23. [@ohos.FusionConnectivity.PartnerAgentExtensionAbility (支持设备状态通知的ExtensionAbility组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-fusionconnectivity-partneragentextensionability)
###### 3.2.2.1.24. tag

###### 3.2.2.1.24.1. [nfctech (标准NFC-Tag Nfc 技术)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-nfctech)
###### 3.2.2.1.24.2. [tagSession (标准NFC-Tag TagSession)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-tagsession)
##### 3.2.2.2. C API

###### 3.2.2.2.1. 模块

###### 3.2.2.2.1.1. [Bluetooth](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-bluetooth)
###### 3.2.2.2.1.2. [Wifi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-wifi)
###### 3.2.2.2.2. 头文件

###### 3.2.2.2.2.1. [oh_bluetooth.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-bluetooth-h)
###### 3.2.2.2.2.2. [oh_wifi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-wifi-h)
##### 3.2.2.3. 错误码

###### 3.2.2.3.1. [蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)
###### 3.2.2.3.2. [WIFI错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-wifi)
###### 3.2.2.3.3. [NFC错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-nfc)
###### 3.2.2.3.4. [SE(secureElement)错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-se)
###### 3.2.2.3.5. [融合短距服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-fusionconnectivity)
##### 3.2.2.4. 已停止维护的接口

###### 3.2.2.4.1. [@ohos.bluetooth (蓝牙)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth)
###### 3.2.2.4.2. [@ohos.bluetoothManager (蓝牙)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager)
###### 3.2.2.4.3. [@ohos.wifi (WLAN)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifi)
###### 3.2.2.4.4. [@ohos.wifiext (WLAN扩展接口)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifiext)
###### 3.2.2.4.5. [@system.bluetooth (蓝牙)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-bluetooth)
#### 3.2.3. Distributed Service Kit（分布式管理服务）

##### 3.2.3.1. ArkTS API

###### 3.2.3.1.1. [@ohos.distributedDeviceManager (设备管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager)
###### 3.2.3.1.2. [@ohos.distributedsched.abilityConnectionManager (应用多端协同管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributed-abilityconnectionmanager)
###### 3.2.3.1.3. [@ohos.application.DistributedExtensionAbility (协同Extension)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributedextensionability)
###### 3.2.3.1.4. [@ohos.distributedsched.linkEnhance (增强连接)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-link-enhance)
###### 3.2.3.1.5. [@ohos.distributedsched.proxyChannelManager (代理通道管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-proxychannelmanager)
##### 3.2.3.2. C API

###### 3.2.3.2.1. 模块

###### 3.2.3.2.1.1. [DeviceManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-devicemanager)
###### 3.2.3.2.2. 头文件

###### 3.2.3.2.2.1. [oh_device_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-device-manager-h)
###### 3.2.3.2.2.2. [oh_device_manager_err_code.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-device-manager-err-code-h)
##### 3.2.3.3. 错误码

###### 3.2.3.3.1. [设备管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-device-manager)
###### 3.2.3.3.2. [增强连接错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-link-enhance)
###### 3.2.3.3.3. [代理通道管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-proxychannelmanager)
#### 3.2.4. NearLink Kit（星闪服务）

##### 3.2.4.1. ArkTS API

###### 3.2.4.1.1. [manager（星闪开关能力）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-manager)
###### 3.2.4.1.2. [remoteDevice（对端设备的连接能力）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-remote-device)
###### 3.2.4.1.3. [advertising（星闪广播能力）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-advertising)
###### 3.2.4.1.4. [scan（星闪扫描能力）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-scan)
###### 3.2.4.1.5. [ssap（星闪SSAP连接能力）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-ssap)
###### 3.2.4.1.6. [dataTransfer（星闪数传能力）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-data-transfer-api)
###### 3.2.4.1.7. [cdsm（星闪合作设备集合能力）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-cdsm)
###### 3.2.4.1.8. [constant（星闪公共常量定义）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-constant)
###### 3.2.4.1.9. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-nearlink)
#### 3.2.5. Network Kit（网络服务）

##### 3.2.5.1. ArkTS API

###### 3.2.5.1.1. [@ohos.net.connection (网络连接管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection)
###### 3.2.5.1.2. [@ohos.net.ethernet (以太网连接管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-ethernet)
###### 3.2.5.1.3. [@ohos.net.http (数据请求)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-http)
###### 3.2.5.1.4. [@ohos.net.mdns (MDNS管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-mdns)
###### 3.2.5.1.5. [@ohos.net.policy (网络策略管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-policy)
###### 3.2.5.1.6. [@ohos.net.socket (Socket连接)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-socket)
###### 3.2.5.1.7. [@ohos.net.statistics (流量管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-statistics)
###### 3.2.5.1.8. [@ohos.net.sharing (网络共享管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-sharing)
###### 3.2.5.1.9. [@ohos.net.vpnExtension (VPN增强管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-vpnextension)
###### 3.2.5.1.10. [@ohos.net.vpn (VPN管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-vpn)
###### 3.2.5.1.11. [@ohos.net.webSocket (WebSocket连接)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-websocket)
###### 3.2.5.1.12. [@ohos.net.netFirewall (网络防火墙)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-netfirewall)
###### 3.2.5.1.13. [@ohos.net.networkSecurity (网络安全校验)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-networksecurity)
###### 3.2.5.1.14. [@ohos.net.eap (扩展认证)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-eap)
###### 3.2.5.1.15. [@ohos.app.ability.VpnExtensionAbility (三方VPN能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-vpnextensionability)
###### 3.2.5.1.16. [VpnExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-vpnextensioncontext)
##### 3.2.5.2. C API

###### 3.2.5.2.1. 模块

###### 3.2.5.2.1.1. [NetConnection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection)
###### 3.2.5.2.1.2. [Netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)
###### 3.2.5.2.2. 头文件

###### 3.2.5.2.2.1. [net_connection.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-h)
###### 3.2.5.2.2.2. [net_connection_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h)
###### 3.2.5.2.2.3. [net_ssl_c.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-ssl-c-h)
###### 3.2.5.2.2.4. [net_ssl_c_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-ssl-c-type-h)
###### 3.2.5.2.2.5. [net_websocket.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-websocket-h)
###### 3.2.5.2.2.6. [net_websocket_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-websocket-type-h)
###### 3.2.5.2.2.7. [net_http.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-h)
###### 3.2.5.2.2.8. [net_http_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h)
###### 3.2.5.2.2.9. [http_interceptor.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-interceptor-h)
###### 3.2.5.2.2.10. [http_interceptor_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-interceptor-type-h)
###### 3.2.5.2.3. 结构体

###### 3.2.5.2.3.1. [NetConn_NetHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-nethandle)
###### 3.2.5.2.3.2. [NetConn_NetCapabilities](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-netcapabilities)
###### 3.2.5.2.3.3. [NetConn_NetAddr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-netaddr)
###### 3.2.5.2.3.4. [NetConn_Route](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-route)
###### 3.2.5.2.3.5. [NetConn_HttpProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-httpproxy)
###### 3.2.5.2.3.6. [NetConn_ConnectionProperties](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-connectionproperties)
###### 3.2.5.2.3.7. [NetConn_NetHandleList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-nethandlelist)
###### 3.2.5.2.3.8. [NetConn_NetSpecifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-netspecifier)
###### 3.2.5.2.3.9. [NetConn_NetConnCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-netconncallback)
###### 3.2.5.2.3.10. [NetConn_ProbeResultInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-proberesultinfo)
###### 3.2.5.2.3.11. [NetConn_TraceRouteInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-tracerouteinfo)
###### 3.2.5.2.3.12. [NetConn_TraceRouteOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-tracerouteoption)
###### 3.2.5.2.3.13. [NetStack_CertBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-netstack-certblob)
###### 3.2.5.2.3.14. [NetStack_CertificatePinning](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-netstack-certificatepinning)
###### 3.2.5.2.3.15. [NetStack_Certificates](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-netstack-certificates)
###### 3.2.5.2.3.16. [WebSocket](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket)
###### 3.2.5.2.3.17. [WebSocket_CloseResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-closeresult)
###### 3.2.5.2.3.18. [WebSocket_CloseOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-closeoption)
###### 3.2.5.2.3.19. [WebSocket_ErrorResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-errorresult)
###### 3.2.5.2.3.20. [WebSocket_OpenResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-openresult)
###### 3.2.5.2.3.21. [WebSocket_Header](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-header)
###### 3.2.5.2.3.22. [WebSocket_RequestOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-requestoptions)
###### 3.2.5.2.3.23. [Http_Buffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-buffer)
###### 3.2.5.2.3.24. [Http_HeaderValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-headervalue)
###### 3.2.5.2.3.25. [Http_HeaderEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-headerentry)
###### 3.2.5.2.3.26. [Http_ClientCert](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-clientcert)
###### 3.2.5.2.3.27. [Http_CustomProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-customproxy)
###### 3.2.5.2.3.28. [Http_Proxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-proxy)
###### 3.2.5.2.3.29. [Http_PerformanceTiming](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-performancetiming)
###### 3.2.5.2.3.30. [Http_RequestOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-requestoptions)
###### 3.2.5.2.3.31. [Http_Response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-response)
###### 3.2.5.2.3.32. [Http_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-request)
###### 3.2.5.2.3.33. [Http_EventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-eventshandler)
###### 3.2.5.2.3.34. [Http_Headers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-headers)
###### 3.2.5.2.3.35. [OH_Http_Interceptor_Headers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-interceptor-headers)
###### 3.2.5.2.3.36. [OH_Http_Interceptor_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-interceptor-request)
###### 3.2.5.2.3.37. [OH_Http_Interceptor_Response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-interceptor-response)
###### 3.2.5.2.3.38. [OH_Http_Interceptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-interceptor)
##### 3.2.5.3. 已停止维护的接口

###### 3.2.5.3.1. [@system.network (网络状态)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-network)
###### 3.2.5.3.2. [@system.fetch (数据请求)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-fetch)
##### 3.2.5.4. 错误码

###### 3.2.5.4.1. [HTTP错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-http)
###### 3.2.5.4.2. [Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)
###### 3.2.5.4.3. [webSocket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-websocket)
###### 3.2.5.4.4. [网络连接管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-connection)
###### 3.2.5.4.5. [以太网连接错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-ethernet)
###### 3.2.5.4.6. [扩展认证错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-eap)
###### 3.2.5.4.7. [网络共享错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-sharing)
###### 3.2.5.4.8. [策略管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-policy)
###### 3.2.5.4.9. [MDNS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-mdns)
###### 3.2.5.4.10. [流量管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-statistics)
###### 3.2.5.4.11. [VPN错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-vpn)
###### 3.2.5.4.12. [网络安全校验错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-networksecurity)
###### 3.2.5.4.13. [内核错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-kernel)
###### 3.2.5.4.14. [防火墙错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-netfirewall)
#### 3.2.6. Network Boost Kit（网络加速服务）

##### 3.2.6.1. ArkTS API

###### 3.2.6.1.1. [netQuality（网络质量）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/networkboost-netquality)
###### 3.2.6.1.2. [netHandover（连接迁移）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/networkboost-nethandover)
###### 3.2.6.1.3. [netBoost（网络加速）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/networkboost-netboost)
###### 3.2.6.1.4. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-networkboost)
##### 3.2.6.2. C API

###### 3.2.6.2.1. 模块

###### 3.2.6.2.1.1. [NetworkBoost](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview)
###### 3.2.6.2.2. 头文件

###### 3.2.6.2.2.1. [network_boost_handover.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-files-handover)
###### 3.2.6.2.2.2. [network_boost_quality.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-files-quality)
###### 3.2.6.2.2.3. [network_boost.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-files-boost)
###### 3.2.6.2.3. 结构体

###### 3.2.6.2.3.1. [HMS_NetworkBoost_HandoverCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-handover_callback)
###### 3.2.6.2.3.2. [NetworkBoost_DataSpeedAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-data_speed_action)
###### 3.2.6.2.3.3. [NetworkBoost_HandoverComplete](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-handover_complete)
###### 3.2.6.2.3.4. [NetworkBoost_HandoverStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-handover_start)
###### 3.2.6.2.3.5. [NetworkBoost_NetHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-net_handle)
###### 3.2.6.2.3.6. [NetworkBoost_NetworkQos](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-network_qos)
###### 3.2.6.2.3.7. [NetworkBoost_NetworkQosArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-network_qos_array)
###### 3.2.6.2.3.8. [NetworkBoost_NetworkScene](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-network_scene)
###### 3.2.6.2.3.9. [NetworkBoost_WeakSignalPrediction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-weak_signal_prediction)
###### 3.2.6.2.3.10. [NetworkBoost_MultiPathQuota](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-multipath_quota)
###### 3.2.6.2.3.11. [NetworkBoost_MultiPathQuotaInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-multipath_quotainfo)
###### 3.2.6.2.3.12. [NetworkBoost_MultiPathRecommendation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-multipath_reco)
###### 3.2.6.2.3.13. [NetworkBoost_MultiPathRequestResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-multipath_req_result)
###### 3.2.6.2.3.14. [NetworkBoost_MultiPathStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-multipath_statechange)
###### 3.2.6.2.3.15. [NetworkBoost_SceneDesc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-scene_desc)
#### 3.2.7. Remote Communication Kit（远场通信服务）

##### 3.2.7.1. ArkTS API

###### 3.2.7.1.1. [rcp（数据请求）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-rcp)
###### 3.2.7.1.2. [urpc（高性能rpc通信库）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-urpcapi)
##### 3.2.7.2. C API

###### 3.2.7.2.1. 模块

###### 3.2.7.2.1.1. [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
###### 3.2.7.2.2. 头文件

###### 3.2.7.2.2.1. [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
###### 3.2.7.2.2.2. [rcp_quic.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_quic_h)
###### 3.2.7.2.3. 结构体

###### 3.2.7.2.3.1. [Rcp_Buffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___buffer)
###### 3.2.7.2.3.2. [Rcp_CertificateAuthority](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___certificate_authority)
###### 3.2.7.2.3.3. [Rcp_ClientCertificate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___client_certificate)
###### 3.2.7.2.3.4. [Rcp_Configuration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___configuration)
###### 3.2.7.2.3.5. [Rcp_ConnectionConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___connection_configuration)
###### 3.2.7.2.3.6. [Rcp_ContentOrPathOrCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___content_or_path_or_callback)
###### 3.2.7.2.3.7. [Rcp_CookieAttributeEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___cookie_attribute_entry)
###### 3.2.7.2.3.8. [Rcp_Credential](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___credential)
###### 3.2.7.2.3.9. [Rcp_DebugInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___debug_info)
###### 3.2.7.2.3.10. [Rcp_DnsConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_configuration)
###### 3.2.7.2.3.11. [Rcp_DnsOverHttps](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_over_https)
###### 3.2.7.2.3.12. [Rcp_DnsRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_rule)
###### 3.2.7.2.3.13. [Rcp_DnsServers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_servers)
###### 3.2.7.2.3.14. [Rcp_EventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___events_handler)
###### 3.2.7.2.3.15. [Rcp_Exclusions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___exclusions)
###### 3.2.7.2.3.16. [Rcp_FormFieldFileValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_file_value)
###### 3.2.7.2.3.17. [Rcp_FormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_value)
###### 3.2.7.2.3.18. [Rcp_FormOrder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_order)
###### 3.2.7.2.3.19. [Rcp_HeaderEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___header_entry)
###### 3.2.7.2.3.20. [Rcp_HeaderValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___header_value)
###### 3.2.7.2.3.21. [Rcp_InfoToCollect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___info_to_collect)
###### 3.2.7.2.3.22. [Rcp_Interceptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___interceptor)
###### 3.2.7.2.3.23. [Rcp_InterceptorArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___interceptor_array)
###### 3.2.7.2.3.24. [Rcp_IpAddress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___ip_address)
###### 3.2.7.2.3.25. [Rcp_IpAndPort](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___ip_and_port)
###### 3.2.7.2.3.26. [Rcp_MultipartFormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value)
###### 3.2.7.2.3.27. [Rcp_OnDataReceiveCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_data_receive_callback)
###### 3.2.7.2.3.28. [Rcp_OnHeaderReceiveCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_header_receive_callback)
###### 3.2.7.2.3.29. [Rcp_OnProgressCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_progress_callback)
###### 3.2.7.2.3.30. [Rcp_OnVoidCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_void_callback)
###### 3.2.7.2.3.31. [Rcp_ProxyConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___proxy_configuration)
###### 3.2.7.2.3.32. [Rcp_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request)
###### 3.2.7.2.3.33. [Rcp_RequestContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request_content)
###### 3.2.7.2.3.34. [Rcp_RequestCookieEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request_cookie_entry)
###### 3.2.7.2.3.35. [Rcp_Response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response)
###### 3.2.7.2.3.36. [Rcp_ResponseCallbackObject](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response_callback_object)
###### 3.2.7.2.3.37. [Rcp_ResponseCookies](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response_cookies)
###### 3.2.7.2.3.38. [Rcp_SecurityConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___security_configuration)
###### 3.2.7.2.3.39. [Rcp_ServerAuthentication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___server_authentication)
###### 3.2.7.2.3.40. [Rcp_SessionConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___session_configuration)
###### 3.2.7.2.3.41. [Rcp_SessionListener](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___session_listener)
###### 3.2.7.2.3.42. [Rcp_StaticDnsRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___static_dns_rule)
###### 3.2.7.2.3.43. [Rcp_StaticDnsRuleItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___static_dns_rule_item)
###### 3.2.7.2.3.44. [Rcp_SyncInterceptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___sync_interceptor)
###### 3.2.7.2.3.45. [Rcp_SyncInterceptorArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___sync_interceptor_array)
###### 3.2.7.2.3.46. [Rcp_TimeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___time_info)
###### 3.2.7.2.3.47. [Rcp_Timeout](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___timeout)
###### 3.2.7.2.3.48. [Rcp_TracingConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___tracing_configuration)
###### 3.2.7.2.3.49. [Rcp_TransferConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___transfer_configuration)
###### 3.2.7.2.3.50. [Rcp_TransferRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___transfer_range)
###### 3.2.7.2.3.51. [Rcp_Urls](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___urls)
###### 3.2.7.2.3.52. [Rcp_WebProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___web_proxy)
###### 3.2.7.2.3.53. [Rcp_OnBinaryReceiveCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_binary_receive_callback)
###### 3.2.7.2.3.54. [Rcp_OnStatusCodeReceiveCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_status_code_callback)
###### 3.2.7.2.3.55. [Rcp_OnGetDataCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_get_data_callback)
###### 3.2.7.2.3.56. [Rcp_QuicSlist](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___quic_slist)
###### 3.2.7.2.3.57. [Rcp_QuicIpAddress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___quic_ipaddress)
###### 3.2.7.2.3.58. [Rcp_QuicIoVec](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___quic_io_vec)
###### 3.2.7.2.3.59. [Rcp_QuicStreamData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___quic_stream_data)
##### 3.2.7.3. [API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-remote-communication)
#### 3.2.8. Service Collaboration Kit（协同服务）

##### 3.2.8.1. ArkTS组件

###### 3.2.8.1.1. [CollaborationCamera (跨设备互通组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-collaborationcamera)
###### 3.2.8.1.2. [CollaborationService (跨设备互通组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-collaborationservice)
###### 3.2.8.1.3. [CollaborationDevicePicker (流转控件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-collaborationdevicepicker)
###### 3.2.8.1.4. [devicePicker (设备选择控制器)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-devicepicker)
###### 3.2.8.1.5. [ArkTS 错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-servicecollaboration)
##### 3.2.8.2. C API

###### 3.2.8.2.1. 模块

###### 3.2.8.2.1.1. [ServiceCollaboration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module)
###### 3.2.8.2.2. 头文件和结构体

####### 3.2.8.2.2.1. 头文件

###### 3.2.8.2.2.1.1. [service_collaboration_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-h)
####### 3.2.8.2.2.2. 结构体

###### 3.2.8.2.2.2.1. [ServiceCollaboration_CollaborationDeviceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-collaborationdeviceinfo)
###### 3.2.8.2.2.2.2. [ServiceCollaboration_CollaborationDeviceInfoSets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-collaborationdeviceinfosets)
###### 3.2.8.2.2.2.3. [ServiceCollaboration_SelectInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-selectinfo)
###### 3.2.8.2.2.2.4. [ServiceCollaborationCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaborationcallback)
###### 3.2.8.2.2.2.5. [ServiceCollaboration_SelectInfoV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-selectinfov2)
#### 3.2.9. Telephony Kit（蜂窝通信服务）

##### 3.2.9.1. ArkTS API

###### 3.2.9.1.1. [@ohos.telephony.call (拨打电话)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-call)
###### 3.2.9.1.2. [@ohos.telephony.data (蜂窝数据)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-telephony-data)
###### 3.2.9.1.3. [@ohos.telephony.esim (eSIM卡管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-esim)
###### 3.2.9.1.4. [@ohos.telephony.observer (observer)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-observer)
###### 3.2.9.1.5. [@ohos.telephony.radio (网络搜索)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-radio)
###### 3.2.9.1.6. [@ohos.telephony.sim (SIM卡管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sim)
###### 3.2.9.1.7. [@ohos.telephony.sms (短信服务)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sms)
###### 3.2.9.1.8. [@ohos.telephony.vcard (VCard模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-vcard)
##### 3.2.9.2. C API

###### 3.2.9.2.1. 模块

###### 3.2.9.2.1.1. [Telephony](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-telephony)
###### 3.2.9.2.2. 头文件

###### 3.2.9.2.2.1. [telephony_data.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-telephony-data-h)
###### 3.2.9.2.2.2. [telephony_radio.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-telephony-radio-h)
###### 3.2.9.2.2.3. [telephony_radio_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-telephony-radio-type-h)
###### 3.2.9.2.3. 结构体

###### 3.2.9.2.3.1. [Telephony_NetworkState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-telephony-telephony-networkstate)
##### 3.2.9.3. 错误码

###### 3.2.9.3.1. [电话子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony)
### 3.3. 基础功能

#### 3.3.1. Basic Services Kit（基础服务）

##### 3.3.1.1. ArkTS API

###### 3.3.1.1.1. 账号管理

###### 3.3.1.1.1.1. [@ohos.account.appAccount (应用账号管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-appaccount)
###### 3.3.1.1.1.2. [@ohos.account.distributedAccount (分布式账号管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributed-account)
###### 3.3.1.1.1.3. [@ohos.account.osAccount (系统账号管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-osaccount)
###### 3.3.1.1.2. 设备管理

###### 3.3.1.1.2.1. [@ohos.batteryInfo (电量信息)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-battery-info)
###### 3.3.1.1.2.2. [@ohos.deviceInfo (设备信息)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-device-info)
###### 3.3.1.1.2.3. [@ohos.power (系统电源管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-power)
###### 3.3.1.1.2.4. [@ohos.runningLock (RunningLock锁)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-runninglock)
###### 3.3.1.1.2.5. [@ohos.thermal (热管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-thermal)
###### 3.3.1.1.2.6. [@ohos.usbManager (USB管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-usbmanager)
###### 3.3.1.1.2.7. [@ohos.usbManager.serial (串口管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-serialmanager)
###### 3.3.1.1.3. 数据文件处理

###### 3.3.1.1.3.1. [@ohos.app.ability.PrintExtensionAbility (打印扩展能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-printextensionability)
###### 3.3.1.1.3.2. [@ohos.pasteboard (剪贴板)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pasteboard)
###### 3.3.1.1.3.3. [@ohos.print (打印)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-print)
###### 3.3.1.1.3.4. [@ohos.scan (扫描)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-scan)
###### 3.3.1.1.3.5. [@ohos.request (上传下载)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-request)
###### 3.3.1.1.3.6. [@ohos.request.cacheDownload (缓存下载)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-request-cachedownload)
###### 3.3.1.1.3.7. [@ohos.zlib (Zip模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-zlib)
###### 3.3.1.1.3.8. [@ohos.selectionInput.SelectionExtensionAbility (划词扩展能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-selectioninput-selectionextensionability)
###### 3.3.1.1.3.9. [@ohos.selectionInput.SelectionExtensionContext (划词扩展上下文)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-selectioninput-selectionextensioncontext)
###### 3.3.1.1.3.10. [@ohos.selectionInput.selectionManager (划词管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-selectioninput-selectionmanager)
###### 3.3.1.1.3.11. [@ohos.selectionInput.SelectionPanel (划词面板)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-selectioninput-selectionpanel)
###### 3.3.1.1.4. 进程线程通信

###### 3.3.1.1.4.1. [系统定义的公共事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/commoneventmanager-definitions)
###### 3.3.1.1.4.2. [@ohos.commonEventManager (公共事件模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-commoneventmanager)
###### 3.3.1.1.4.3. [@ohos.events.emitter (Emitter)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-emitter)
####### 3.3.1.1.4.4. commonEvent

###### 3.3.1.1.4.4.1. [CommonEventData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-commonevent-commoneventdata)
###### 3.3.1.1.4.4.2. [CommonEventPublishData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-commonevent-commoneventpublishdata)
###### 3.3.1.1.4.4.3. [commonEventSubscriber](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-commonevent-commoneventsubscriber)
###### 3.3.1.1.4.4.4. [CommonEventSubscribeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-commonevent-commoneventsubscribeinfo)
###### 3.3.1.1.5. 其他

###### 3.3.1.1.5.1. [@ohos.base (公共回调信息)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base)
###### 3.3.1.1.5.2. [@ohos.annotation (注解)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-annotation)
###### 3.3.1.1.5.3. [@ohos.customization.customConfig (定制配置)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-customization-customconfig)
###### 3.3.1.1.5.4. [@ohos.settings (设置数据项名称)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-settings)
###### 3.3.1.1.5.5. [@ohos.wallpaper (壁纸)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wallpaper)
###### 3.3.1.1.5.6. [@ohos.resourceschedule.systemload (性能功耗热融合档位)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-systemload)
###### 3.3.1.1.5.7. [@ohos.systemDateTime (系统时间、时区)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-date-time)
###### 3.3.1.1.5.8. [@ohos.intelligentScene (情景模式)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-intelligentscene)
###### 3.3.1.1.6. 已停止维护的接口

###### 3.3.1.1.6.1. [系统公共事件定义 (已废弃)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/commonevent-definitions)
###### 3.3.1.1.6.2. [@ohos.commonEvent (公共事件模块)(已废弃)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-commonevent)
###### 3.3.1.1.6.3. [@ohos.usb (USB管理)(已停止维护)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-usb-deprecated)
###### 3.3.1.1.6.4. [@system.brightness (屏幕亮度)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-brightness)
###### 3.3.1.1.6.5. [@system.battery (电量信息)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-battery)
###### 3.3.1.1.6.6. [@system.device (设备信息)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-device)
###### 3.3.1.1.6.7. [@system.request (上传下载)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-request)
###### 3.3.1.1.6.8. [@ohos.screenLock (锁屏管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-screen-lock)
###### 3.3.1.1.6.9. [@ohos.systemTime (系统时间、时区)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-time)
##### 3.3.1.2. C API

###### 3.3.1.2.1. 模块

###### 3.3.1.2.1.1. [OH_CommonEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent)
###### 3.3.1.2.1.2. [DeviceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-deviceinfo)
###### 3.3.1.2.1.3. [OsAccount](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-osaccount)
###### 3.3.1.2.1.4. [OH_BatteryInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-batteryinfo)
###### 3.3.1.2.1.5. [OH_Scan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-scan)
###### 3.3.1.2.1.6. [OH_Print](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print)
###### 3.3.1.2.1.7. [Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard)
###### 3.3.1.2.1.8. [TimeService](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-timeservice)
###### 3.3.1.2.2. 头文件

###### 3.3.1.2.2.1. [deviceinfo.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-deviceinfo-h)
###### 3.3.1.2.2.2. [ohbattery_info.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohbattery-info-h)
###### 3.3.1.2.2.3. [oh_commonevent.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h)
###### 3.3.1.2.2.4. [oh_commonevent_support.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-support-h)
###### 3.3.1.2.2.5. [oh_pasteboard.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-h)
###### 3.3.1.2.2.6. [oh_pasteboard_err_code.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-err-code-h)
###### 3.3.1.2.2.7. [os_account.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-os-account-h)
###### 3.3.1.2.2.8. [os_account_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-os-account-common-h)
###### 3.3.1.2.2.9. [ohprint.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohprint-h)
###### 3.3.1.2.2.10. [ohscan.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohscan-h)
###### 3.3.1.2.2.11. [time_service.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-time-service-h)
###### 3.3.1.2.3. 结构体

###### 3.3.1.2.3.1. [CommonEvent_SubscribeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-commonevent-subscribeinfo)
###### 3.3.1.2.3.2. [CommonEvent_PublishInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-commonevent-publishinfo)
###### 3.3.1.2.3.3. [CommonEvent_RcvData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-commonevent-rcvdata)
###### 3.3.1.2.3.4. [Pasteboard_ProgressInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-progressinfo)
###### 3.3.1.2.3.5. [Pasteboard_GetDataParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-getdataparams)
###### 3.3.1.2.3.6. [OH_PasteboardObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboardobserver)
###### 3.3.1.2.3.7. [OH_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)
###### 3.3.1.2.3.8. [Print_Margin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-margin)
###### 3.3.1.2.3.9. [Print_PageSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-pagesize)
###### 3.3.1.2.3.10. [Print_Range](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-range)
###### 3.3.1.2.3.11. [Print_DefaultValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-defaultvalue)
###### 3.3.1.2.3.12. [Print_PrinterCapability](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-printercapability)
###### 3.3.1.2.3.13. [Print_PrinterInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-printerinfo)
###### 3.3.1.2.3.14. [Print_PrintJob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-printjob)
###### 3.3.1.2.3.15. [Print_Property](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-property)
###### 3.3.1.2.3.16. [Print_PropertyList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-propertylist)
###### 3.3.1.2.3.17. [Print_Resolution](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-resolution)
###### 3.3.1.2.3.18. [Print_StringList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-stringlist)
###### 3.3.1.2.3.19. [Print_PrintAttributes](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-printattributes)
###### 3.3.1.2.3.20. [Print_PrintDocCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-printdoccallback)
###### 3.3.1.2.3.21. [Scan_ScannerDevice](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-scan-scan-scannerdevice)
###### 3.3.1.2.3.22. [Scan_PictureScanProgress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-scan-scan-picturescanprogress)
###### 3.3.1.2.3.23. [Scan_ScannerOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-scan-scan-scanneroptions)
##### 3.3.1.3. 错误码

###### 3.3.1.3.1. [USB服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-usb)
###### 3.3.1.3.2. [RunningLock锁错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-runninglock)
###### 3.3.1.3.3. [zlib子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-zlib)
###### 3.3.1.3.4. [剪贴板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pasteboard)
###### 3.3.1.3.5. [热管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-thermal)
###### 3.3.1.3.6. [上传下载错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-request)
###### 3.3.1.3.7. [时间时区服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-time)
###### 3.3.1.3.8. [事件错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-commoneventservice)
###### 3.3.1.3.9. [系统电源管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-power)
###### 3.3.1.3.10. [账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)
###### 3.3.1.3.11. [打印服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-print)
###### 3.3.1.3.12. [设置数据项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-settings)
###### 3.3.1.3.13. [划词服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-selection)
###### 3.3.1.3.14. [情景模式错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-intelligentscene)
###### 3.3.1.3.15. [deviceInfo错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-device-info)
#### 3.3.2. Desktop Extension Kit（桌面拓展服务）

##### 3.3.2.1. ArkTS API

###### 3.3.2.1.1. [statusBarManager（状态栏管理服务）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/statusbar-extension-manager)
###### 3.3.2.1.2. [StatusBarViewExtensionAbility（状态栏扩展Ability）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/statusbar-extension-ability)
###### 3.3.2.1.3. [quickBarManager（快捷栏管理服务）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/desktop-quickbar-extension-manager)
###### 3.3.2.1.4. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-statusbar-extension)
#### 3.3.3. FAST Kit（算法加速服务）

##### 3.3.3.1. ArkTS API

###### 3.3.3.1.1. [@hms.fast.mathPrediction (数理预测)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-math-prediction)
###### 3.3.3.1.2. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-errorcode)
##### 3.3.3.2. C API

###### 3.3.3.2.1. 模块

###### 3.3.3.2.1.1. [FAST](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast)
###### 3.3.3.2.2. 头文件和结构体

####### 3.3.3.2.2.1. 头文件

###### 3.3.3.2.2.1.1. [fast_ads_concurrent_hashmap.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-ads-concurrent-hashmap-8h)
###### 3.3.3.2.2.1.2. [fast_ads_segment_map.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-ads-segment-map-8h)
###### 3.3.3.2.2.1.3. [fast_common_def.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-common-def-8h)
###### 3.3.3.2.2.1.4. [fast_dsp_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-dsp-common-8h)
###### 3.3.3.2.2.1.5. [fast_dsp_transform.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-dsp-transform-8h)
###### 3.3.3.2.2.1.6. [fast_solver_rect_partition.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-solver-rect-partition-8h)
###### 3.3.3.2.2.1.7. [fast_collections_hashmap.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-collections-hashmap-8h)
####### 3.3.3.2.2.2. 结构体

###### 3.3.3.2.2.2.1. [FAST_BiquadCoefficients](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadcoefficients)
###### 3.3.3.2.2.2.2. [FAST_BiquadCoefficientsD](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadcoefficientsd)
###### 3.3.3.2.2.2.3. [FAST_Biquadm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadm)
###### 3.3.3.2.2.2.4. [FAST_BiquadmD](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadmd)
###### 3.3.3.2.2.2.5. [FAST_BiquadState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadstate)
###### 3.3.3.2.2.2.6. [FAST_BiquadStateD](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadstated)
###### 3.3.3.2.2.2.7. [FAST_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-rect)
###### 3.3.3.2.2.2.8. [FAST_SplitComplex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-splitcomplex)
###### 3.3.3.2.2.2.9. [FAST_SplitComplexD](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-splitcomplexd)
#### 3.3.4. Function Flow Runtime Kit

##### 3.3.4.1. C API

###### 3.3.4.1.1. 模块

###### 3.3.4.1.1.1. [FFRT](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt)
###### 3.3.4.1.2. 头文件

###### 3.3.4.1.2.1. [condition_variable.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-condition-variable-h)
###### 3.3.4.1.2.2. [loop.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-loop-h)
###### 3.3.4.1.2.3. [mutex.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mutex-h)
###### 3.3.4.1.2.4. [queue.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-queue-h)
###### 3.3.4.1.2.5. [shared_mutex.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-shared-mutex-h)
###### 3.3.4.1.2.6. [sleep.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-sleep-h)
###### 3.3.4.1.2.7. [task.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-task-h)
###### 3.3.4.1.2.8. [timer.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-timer-h)
###### 3.3.4.1.2.9. [fiber.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fiber-h)
###### 3.3.4.1.2.10. [type_def.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-type-def-h)
###### 3.3.4.1.3. 结构体

###### 3.3.4.1.3.1. [ffrt_function_header_t](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-function-header-t)
###### 3.3.4.1.3.2. [ffrt_dependence_t](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-dependence-t)
###### 3.3.4.1.3.3. [ffrt_deps_t](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-deps-t)
###### 3.3.4.1.3.4. [ffrt_task_attr_t](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-task-attr-t)
###### 3.3.4.1.3.5. [ffrt_queue_attr_t](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-queue-attr-t)
###### 3.3.4.1.3.6. [ffrt_condattr_t](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-condattr-t)
###### 3.3.4.1.3.7. [ffrt_mutexattr_t](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-mutexattr-t)
###### 3.3.4.1.3.8. [ffrt_rwlockattr_t](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-rwlockattr-t)
###### 3.3.4.1.3.9. [ffrt_mutex_t](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-mutex-t)
###### 3.3.4.1.3.10. [ffrt_rwlock_t](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-rwlock-t)
###### 3.3.4.1.3.11. [ffrt_cond_t](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-cond-t)
###### 3.3.4.1.3.12. [ffrt_loop_t](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-loop-t)
###### 3.3.4.1.3.13. [ffrt_queue_t](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-queue-t)
###### 3.3.4.1.3.14. [ffrt_task_handle_t](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-task-handle-t)
###### 3.3.4.1.3.15. [ffrt_fiber_t](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-fiber-t)
#### 3.3.5. Input Kit（多模输入服务）

##### 3.3.5.1. ArkTS API

###### 3.3.5.1.1. [@ohos.multimodalInput.inputDevice (输入设备)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputdevice)
###### 3.3.5.1.2. [@ohos.multimodalInput.inputEvent (输入事件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputevent)
###### 3.3.5.1.3. [@ohos.multimodalInput.intentionCode (意图事件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-intentioncode)
###### 3.3.5.1.4. [@ohos.multimodalInput.keyCode (键值)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keycode)
###### 3.3.5.1.5. [@ohos.multimodalInput.keyEvent (按键输入事件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keyevent)
###### 3.3.5.1.6. [@ohos.multimodalInput.mouseEvent (鼠标输入事件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-mouseevent)
###### 3.3.5.1.7. [@ohos.multimodalInput.gestureEvent (手势事件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-multimodalinput-gestureevent)
###### 3.3.5.1.8. [@ohos.multimodalInput.pointer (鼠标光标)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pointer)
###### 3.3.5.1.9. [@ohos.multimodalInput.touchEvent (触屏输入事件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-touchevent)
###### 3.3.5.1.10. [@ohos.multimodalInput.infraredEmitter (红外管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-infraredemitter)
###### 3.3.5.1.11. [@ohos.multimodalInput.inputConsumer (全局快捷键)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputconsumer)
###### 3.3.5.1.12. [@ohos.multimodalInput.inputEventClient (输入事件注入)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputeventclient)
##### 3.3.5.2. C API

###### 3.3.5.2.1. 模块

###### 3.3.5.2.1.1. [input](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input)
###### 3.3.5.2.2. 头文件

###### 3.3.5.2.2.1. [oh_axis_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-axis-type-h)
###### 3.3.5.2.2.2. [oh_input_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-input-manager-h)
###### 3.3.5.2.2.3. [oh_key_code.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-key-code-h)
###### 3.3.5.2.2.4. [oh_pointer_style.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pointer-style-h)
###### 3.3.5.2.3. 结构体

###### 3.3.5.2.3.1. [Input_InterceptorEventCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-interceptoreventcallback)
###### 3.3.5.2.3.2. [Input_DeviceListener](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-devicelistener)
###### 3.3.5.2.3.3. [OH_PixelmapNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-oh-pixelmapnative)
###### 3.3.5.2.3.4. [Input_KeyState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-keystate)
###### 3.3.5.2.3.5. [Input_KeyEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-keyevent)
###### 3.3.5.2.3.6. [Input_MouseEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-mouseevent)
###### 3.3.5.2.3.7. [Input_TouchEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-touchevent)
###### 3.3.5.2.3.8. [Input_AxisEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-axisevent)
###### 3.3.5.2.3.9. [Input_Hotkey](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-hotkey)
###### 3.3.5.2.3.10. [Input_DeviceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-deviceinfo)
###### 3.3.5.2.3.11. [Input_InterceptorOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-interceptoroptions)
###### 3.3.5.2.3.12. [Input_CursorConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-cursorconfig)
###### 3.3.5.2.3.13. [Input_CustomCursor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-customcursor)
###### 3.3.5.2.3.14. [Input_CursorInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-cursorinfo)
##### 3.3.5.3. 错误码

###### 3.3.5.3.1. [全局快捷键管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputconsumer)
###### 3.3.5.3.2. [输入设备错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputdevice)
###### 3.3.5.3.3. [鼠标光标错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pointer)
###### 3.3.5.3.4. [红外管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-infraredemitter)
###### 3.3.5.3.5. [输入事件注入错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputeventclient)
#### 3.3.6. MDM Kit（企业设备管理服务）

##### 3.3.6.1. ArkTS API

###### 3.3.6.1.1. [@ohos.enterprise.accountManager（账号管理）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-accountmanager)
###### 3.3.6.1.2. [@ohos.enterprise.adminManager（admin权限管理）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-adminmanager)
###### 3.3.6.1.3. [@ohos.enterprise.applicationManager（应用管理）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-applicationmanager)
###### 3.3.6.1.4. [@ohos.enterprise.bluetoothManager（蓝牙管理）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-bluetoothmanager)
###### 3.3.6.1.5. [@ohos.enterprise.browser（浏览器管理）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-browser)
###### 3.3.6.1.6. [@ohos.enterprise.bundleManager（包管理）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-bundlemanager)
###### 3.3.6.1.7. [@ohos.enterprise.common（Enterprise公共模块）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-common)
###### 3.3.6.1.8. [@ohos.enterprise.deviceControl（设备控制管理）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-devicecontrol)
###### 3.3.6.1.9. [@ohos.enterprise.deviceInfo（设备信息管理）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-deviceinfo)
###### 3.3.6.1.10. [@ohos.enterprise.deviceSettings （设备设置管理）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-devicesettings)
###### 3.3.6.1.11. [@ohos.enterprise.locationManager（位置服务管理）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-locationmanager)
###### 3.3.6.1.12. [@ohos.enterprise.networkManager（网络管理）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-networkmanager)
###### 3.3.6.1.13. [@ohos.enterprise.restrictions （限制类策略）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-restrictions)
###### 3.3.6.1.14. [@ohos.enterprise.securityManager（安全管理）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-securitymanager)
###### 3.3.6.1.15. [@ohos.enterprise.systemManager （系统管理）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-systemmanager)
###### 3.3.6.1.16. [@ohos.enterprise.usbManager（USB管理）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-usbmanager)
###### 3.3.6.1.17. [@ohos.enterprise.wifiManager（Wi-Fi管理）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-wifimanager)
###### 3.3.6.1.18. [@ohos.enterprise.EnterpriseAdminExtensionAbility（企业设备管理扩展能力）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterpriseadminextensionability)
###### 3.3.6.1.19. [@ohos.enterprise.telephonyManager（通话管理）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-telephonymanager)
###### 3.3.6.1.20. application

###### 3.3.6.1.20.1. [EnterpriseAdminExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-enterpriseadminextensioncontext)
##### 3.3.6.2. 错误码

###### 3.3.6.2.1. [企业设备管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-enterprisedevicemanager)
#### 3.3.7. Kernel Enhance Kit（内核增强能力）

##### 3.3.7.1. C API

###### 3.3.7.1.1. 模块

###### 3.3.7.1.1.1. [QoS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-qos)
###### 3.3.7.1.2. 头文件

###### 3.3.7.1.2.1. [qos.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-qos-h)
###### 3.3.7.1.3. 结构体

###### 3.3.7.1.3.1. [OH_QoS_GewuCreateSessionResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-qos-oh-qos-gewucreatesessionresult)
###### 3.3.7.1.3.2. [OH_QoS_GewuSubmitRequestResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-qos-oh-qos-gewusubmitrequestresult)
### 3.4. 硬件

#### 3.4.1. Car Kit（车服务）

##### 3.4.1.1. ArkTS API

###### 3.4.1.1.1. [navigationInfoMgr（导航信息管理）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/car-navigationinfomgr)
###### 3.4.1.1.2. [smartMobilityCommon（智慧出行场景）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/car-smartmobilitycommon)
###### 3.4.1.1.3. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-car)
##### 3.4.1.2. 附录

###### 3.4.1.2.1. [naviTurnMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/car-appendix-naviturnmode)
###### 3.4.1.2.2. [trafficLane](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/car-appendix-trafficlane)
#### 3.4.2. Driver Development Kit（驱动开发服务）

##### 3.4.2.1. ArkTS API

###### 3.4.2.1.1. [@ohos.app.ability.DriverExtensionAbility (驱动程序扩展能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-driverextensionability)
###### 3.4.2.1.2. [@ohos.driver.deviceManager (外设管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-driver-devicemanager)
###### 3.4.2.1.3. application

###### 3.4.2.1.3.1. [DriverExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-driverextensioncontext)
##### 3.4.2.2. C API

###### 3.4.2.2.1. 模块

###### 3.4.2.2.1.1. [BaseDdk](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-baseddk)
###### 3.4.2.2.1.2. [HidDdk](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk)
###### 3.4.2.2.1.3. [ScsiPeripheralDDK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk)
###### 3.4.2.2.1.4. [UsbDdk](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk)
###### 3.4.2.2.1.5. [USBSerialDDK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-serialddk)
###### 3.4.2.2.2. 头文件

###### 3.4.2.2.2.1. [ddk_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ddk-api-h)
###### 3.4.2.2.2.2. [ddk_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ddk-types-h)
###### 3.4.2.2.2.3. [hid_ddk_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hid-ddk-api-h)
###### 3.4.2.2.2.4. [hid_ddk_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hid-ddk-types-h)
###### 3.4.2.2.2.5. [scsi_peripheral_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsi-peripheral-api-h)
###### 3.4.2.2.2.6. [scsi_peripheral_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsi-peripheral-types-h)
###### 3.4.2.2.2.7. [usb_ddk_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usb-ddk-api-h)
###### 3.4.2.2.2.8. [usb_ddk_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usb-ddk-types-h)
###### 3.4.2.2.2.9. [usb_serial_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usb-serial-api-h)
###### 3.4.2.2.2.10. [usb_serial_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usb-serial-types-h)
###### 3.4.2.2.3. 结构体

###### 3.4.2.2.3.1. [DDK_Ashmem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-baseddk-ddk-ashmem)
###### 3.4.2.2.3.2. [Hid_EmitItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-emititem)
###### 3.4.2.2.3.3. [Hid_Device](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-device)
###### 3.4.2.2.3.4. [Hid_EventTypeArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-eventtypearray)
###### 3.4.2.2.3.5. [Hid_KeyCodeArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-keycodearray)
###### 3.4.2.2.3.6. [Hid_AbsAxesArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-absaxesarray)
###### 3.4.2.2.3.7. [Hid_RelAxesArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-relaxesarray)
###### 3.4.2.2.3.8. [Hid_MscEventArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-msceventarray)
###### 3.4.2.2.3.9. [Hid_EventProperties](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-eventproperties)
###### 3.4.2.2.3.10. [Hid_RawDevInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-rawdevinfo)
###### 3.4.2.2.3.11. [Hid_DeviceHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-devicehandle)
###### 3.4.2.2.3.12. [ScsiPeripheral_DeviceMemMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-devicememmap)
###### 3.4.2.2.3.13. [ScsiPeripheral_IORequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-iorequest)
###### 3.4.2.2.3.14. [ScsiPeripheral_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-request)
###### 3.4.2.2.3.15. [ScsiPeripheral_Response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-response)
###### 3.4.2.2.3.16. [ScsiPeripheral_TestUnitReadyRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-testunitreadyrequest)
###### 3.4.2.2.3.17. [ScsiPeripheral_InquiryRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-inquiryrequest)
###### 3.4.2.2.3.18. [ScsiPeripheral_InquiryInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-inquiryinfo)
###### 3.4.2.2.3.19. [ScsiPeripheral_ReadCapacityRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-readcapacityrequest)
###### 3.4.2.2.3.20. [ScsiPeripheral_CapacityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-capacityinfo)
###### 3.4.2.2.3.21. [ScsiPeripheral_RequestSenseRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-requestsenserequest)
###### 3.4.2.2.3.22. [ScsiPeripheral_BasicSenseInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-basicsenseinfo)
###### 3.4.2.2.3.23. [ScsiPeripheral_VerifyRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-verifyrequest)
###### 3.4.2.2.3.24. [ScsiPeripheral_Device](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-device)
###### 3.4.2.2.3.25. [UsbControlRequestSetup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbcontrolrequestsetup)
###### 3.4.2.2.3.26. [UsbDeviceDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbdevicedescriptor)
###### 3.4.2.2.3.27. [UsbConfigDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbconfigdescriptor)
###### 3.4.2.2.3.28. [UsbInterfaceDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbinterfacedescriptor)
###### 3.4.2.2.3.29. [UsbEndpointDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbendpointdescriptor)
###### 3.4.2.2.3.30. [UsbDdkEndpointDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbddkendpointdescriptor)
###### 3.4.2.2.3.31. [UsbDdkInterfaceDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbddkinterfacedescriptor)
###### 3.4.2.2.3.32. [UsbDdkInterface](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbddkinterface)
###### 3.4.2.2.3.33. [UsbDdkConfigDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbddkconfigdescriptor)
###### 3.4.2.2.3.34. [UsbRequestPipe](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbrequestpipe)
###### 3.4.2.2.3.35. [UsbDeviceMemMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbdevicememmap)
###### 3.4.2.2.3.36. [Usb_DeviceArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usb-devicearray)
###### 3.4.2.2.3.37. [Usb_NonRootHubArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usb-nonroothubarray)
###### 3.4.2.2.3.38. [UsbSerial_Params](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-serialddk-usbserial-params)
###### 3.4.2.2.3.39. [UsbSerial_Device](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-serialddk-usbserial-devicehandle)
##### 3.4.2.3. 错误码

###### 3.4.2.3.1. [驱动错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicemanager)
#### 3.4.3. Multimodal Awareness Kit（多模态融合感知服务）

##### 3.4.3.1. ArkTS API

###### 3.4.3.1.1. [@ohos.stationary (设备状态感知框架)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-stationary)
###### 3.4.3.1.2. [@ohos.multimodalAwareness.motion (动作感知能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-awareness-motion)
###### 3.4.3.1.3. [@ohos.multimodalAwareness.metadataBinding (记忆链接)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-awareness-metadatabinding)
###### 3.4.3.1.4. [@ohos.multimodalAwareness.deviceStatus (设备状态感知)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-awareness-devicestatus)
###### 3.4.3.1.5. [@ohos.multimodalAwareness.userStatus (用户状态感知)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-awareness-userstatus)
##### 3.4.3.2. 错误码

###### 3.4.3.2.1. [动作感知错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-motion)
###### 3.4.3.2.2. [记忆链接错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-metadatabinding)
###### 3.4.3.2.3. [设备状态感知错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicestatus)
###### 3.4.3.2.4. [用户状态感知错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-userstatus)
#### 3.4.4. Pen Kit（手写笔服务）

##### 3.4.4.1. ArkTS API

###### 3.4.4.1.1. [HandwriteController (手写套件功能)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwritecontroller)
###### 3.4.4.1.2. [PointPredictor（报点预测功能）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-pointpredictor)
###### 3.4.4.1.3. [InstantShapeGenerator（一笔成形功能）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-instantsshapegenerator)
###### 3.4.4.1.4. [imageFeaturePicker (全局取色功能)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-imagefeaturepicker)
###### 3.4.4.1.5. [stylusInteraction (手写笔交互功能)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-stylusinteraction)
##### 3.4.4.2. ArkTS组件

###### 3.4.4.2.1. [HandwriteComponent（手写套件组件）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwritecomponent)
##### 3.4.4.3. C API

###### 3.4.4.3.1. 模块

###### 3.4.4.3.1.1. [GlobalColorPicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-imagefeaturepicker-c)
###### 3.4.4.3.1.2. [HandWrite](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwrite-c)
###### 3.4.4.3.2. 头文件和结构体

####### 3.4.4.3.2.1. 头文件

###### 3.4.4.3.2.1.1. [native_gcp_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-headerfile-declare)
###### 3.4.4.3.2.1.2. [native_handwrite_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwrite-headerfile-declare)
####### 3.4.4.3.2.2. 结构体

###### 3.4.4.3.2.2.1. [HMS_GCP_Color](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-imagefeaturepicker-struct-color)
###### 3.4.4.3.2.2.2. [HMS_GCP_PickedColorInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-imagefeaturepicker-struct-colorinfo)
###### 3.4.4.3.2.2.3. [HandWrite_HistoricalPoint](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwrite-struct-historicalpoint)
##### 3.4.4.4. [ArkTS API 错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pen)
#### 3.4.5. Sensor Service Kit（传感器服务）

##### 3.4.5.1. ArkTS API

###### 3.4.5.1.1. [@ohos.sensor (传感器)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sensor)
###### 3.4.5.1.2. [@ohos.vibrator (振动)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-vibrator)
###### 3.4.5.1.3. [@system.sensor (传感器)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-sensor)
###### 3.4.5.1.4. [@system.vibrator (振动)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-vibrate)
##### 3.4.5.2. C API

###### 3.4.5.2.1. 模块

###### 3.4.5.2.1.1. [Sensor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-sensor)
###### 3.4.5.2.1.2. [Vibrator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vibrator)
###### 3.4.5.2.2. 头文件

###### 3.4.5.2.2.1. [oh_sensor.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-sensor-h)
###### 3.4.5.2.2.2. [oh_sensor_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-sensor-type-h)
###### 3.4.5.2.2.3. [vibrator.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vibrator-h)
###### 3.4.5.2.2.4. [vibrator_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vibrator-type-h)
###### 3.4.5.2.3. 结构体

###### 3.4.5.2.3.1. [Sensor_Info](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-sensor-sensor-info)
###### 3.4.5.2.3.2. [Sensor_Event](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-sensor-sensor-event)
###### 3.4.5.2.3.3. [Sensor_SubscriptionId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-sensor-sensor-subscriptionid)
###### 3.4.5.2.3.4. [Sensor_SubscriptionAttribute](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-sensor-sensor-subscriptionattribute)
###### 3.4.5.2.3.5. [Sensor_Subscriber](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-sensor-sensor-subscriber)
###### 3.4.5.2.3.6. [Vibrator_Attribute](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vibrator-vibrator-attribute)
###### 3.4.5.2.3.7. [Vibrator_FileDescription](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vibrator-vibrator-filedescription)
##### 3.4.5.3. 错误码

###### 3.4.5.3.1. [传感器错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-sensor)
###### 3.4.5.3.2. [振动错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-vibrator)
#### 3.4.6. Mechanic Kit（机械设备管理服务）

##### 3.4.6.1. ArkTS API

###### 3.4.6.1.1. [@ohos.distributedHardware.mechanicManager (机械体控制模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-mechanicmanager)
##### 3.4.6.2. 错误码

###### 3.4.6.2.1. [机械体控制模块错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-mechanic)
#### 3.4.7. Wear Engine Kit（穿戴服务）

##### 3.4.7.1. ArkTS API

###### 3.4.7.1.1. [wearEngine（穿戴设备能力开放）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api)
###### 3.4.7.1.2. [wearEngineLite（穿戴设备能力开放）（Lite）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearenginelite_api)
##### 3.4.7.2. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-wearengine)
### 3.5. 调测调优

#### 3.5.1. Performance Analysis Kit（性能分析服务）

##### 3.5.1.1. ArkTS API

###### 3.5.1.1.1. [@ohos.hichecker (检测模式)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hichecker)
###### 3.5.1.1.2. [@ohos.hidebug (Debug调试)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hidebug)
###### 3.5.1.1.3. [@ohos.hilog (HiLog日志打印)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hilog)
###### 3.5.1.1.4. [@ohos.hiTraceChain (分布式跟踪)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hitracechain)
###### 3.5.1.1.5. [@ohos.hiTraceMeter (性能打点)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hitracemeter)
###### 3.5.1.1.6. [@ohos.hiviewdfx.FaultLogExtensionAbility (故障延迟通知)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-faultlogextensionability)
###### 3.5.1.1.7. [@ohos.hiviewdfx.FaultLogExtensionContext (故障延迟通知上下文)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-faultlogextensioncontext)
###### 3.5.1.1.8. [@ohos.hiviewdfx.hiAppEvent (应用事件打点)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-hiappevent)
###### 3.5.1.1.9. [@ohos.hiviewdfx.hiRetrieval (应用灰度)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiretrieval)
###### 3.5.1.1.10. [@ohos.hiviewdfx.jsLeakWatcher (ArkTS泄漏检测)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-jsleakwatcher)
###### 3.5.1.1.11. 已停止维护的接口

###### 3.5.1.1.11.1. [@ohos.bytrace (性能打点)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bytrace)
###### 3.5.1.1.11.2. [@ohos.hiAppEvent (应用打点)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiappevent)
###### 3.5.1.1.11.3. [@ohos.faultLogger (故障日志获取)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-faultlogger)
##### 3.5.1.2. C API

###### 3.5.1.2.1. 模块

###### 3.5.1.2.1.1. [HiAppEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent)
###### 3.5.1.2.1.2. [HiCollie](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hicollie)
###### 3.5.1.2.1.3. [HiDebug](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug)
###### 3.5.1.2.1.4. [HiLog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hilog)
###### 3.5.1.2.1.5. [HiTrace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hitrace)
###### 3.5.1.2.2. 头文件

###### 3.5.1.2.2.1. [hiappevent.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-h)
###### 3.5.1.2.2.2. [hiappevent_cfg.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-cfg-h)
###### 3.5.1.2.2.3. [hiappevent_event.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-event-h)
###### 3.5.1.2.2.4. [hiappevent_param.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-param-h)
###### 3.5.1.2.2.5. [hicollie.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hicollie-h)
###### 3.5.1.2.2.6. [hidebug.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-h)
###### 3.5.1.2.2.7. [hidebug_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-type-h)
###### 3.5.1.2.2.8. [log.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-log-h)
###### 3.5.1.2.2.9. [trace.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trace-h)
###### 3.5.1.2.3. 结构体

###### 3.5.1.2.3.1. [HiAppEvent_AppEventInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-hiappevent-appeventinfo)
###### 3.5.1.2.3.2. [HiAppEvent_AppEventGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-hiappevent-appeventgroup)
###### 3.5.1.2.3.3. [ParamListNode*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-paramlistnode8h)
###### 3.5.1.2.3.4. [HiAppEvent_Watcher](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-hiappevent-watcher)
###### 3.5.1.2.3.5. [HiAppEvent_Processor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-hiappevent-processor)
###### 3.5.1.2.3.6. [HiAppEvent_Config](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-hiappevent-config)
###### 3.5.1.2.3.7. [HiCollie_DetectionParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hicollie-hicollie-detectionparam)
###### 3.5.1.2.3.8. [HiCollie_SetTimerParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hicollie-hicollie-settimerparam)
###### 3.5.1.2.3.9. [HiDebug_ThreadCpuUsage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-threadcpuusage)
###### 3.5.1.2.3.10. [HiDebug_SystemMemInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-systemmeminfo)
###### 3.5.1.2.3.11. [HiDebug_NativeMemInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-nativememinfo)
###### 3.5.1.2.3.12. [HiDebug_MemoryLimit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-memorylimit)
###### 3.5.1.2.3.13. [OH_HiDebug_RequestTraceConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-oh-hidebug-requesttraceconfig)
###### 3.5.1.2.3.14. [HiDebug_JsStackFrame](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-jsstackframe)
###### 3.5.1.2.3.15. [HiDebug_NativeStackFrame](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-nativestackframe)
###### 3.5.1.2.3.16. [HiDebug_StackFrame](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-stackframe)
###### 3.5.1.2.3.17. [HiDebug_MallocDispatch](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-mallocdispatch)
###### 3.5.1.2.3.18. [HiDebug_Backtrace_Object__*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-backtrace-object--8h)
###### 3.5.1.2.3.19. [HiDebug_GraphicsMemorySummary](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-graphicsmemorysummary)
###### 3.5.1.2.3.20. [HiDebug_ProcessSamplerConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-processsamplerconfig)
###### 3.5.1.2.3.21. [OH_HiDebug_ResProfilerConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-oh-hidebug-resprofilerconfig)
###### 3.5.1.2.3.22. [OH_HiDebug_ProfilingResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-oh-hidebug-profilingresult)
###### 3.5.1.2.3.23. [HiTraceId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hitrace-hitraceid)
##### 3.5.1.3. 错误码

###### 3.5.1.3.1. [Faultlogger 错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-faultlogger)
###### 3.5.1.3.2. [应用事件打点错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-hiappevent)
###### 3.5.1.3.3. [HiDebug错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-hiviewdfx-hidebug)
###### 3.5.1.3.4. [HiDebug CpuUsage错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-hiviewdfx-hidebug-cpuusage)
###### 3.5.1.3.5. [HiDebug Trace错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-hiviewdfx-hidebug-trace)
###### 3.5.1.3.6. [HiCollie错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-hiviewdfx-hicollie)
###### 3.5.1.3.7. [JsLeakWatcher错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-jsleakwatcher)
###### 3.5.1.3.8. [应用灰度错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-hiviewdfx-hiretrieval)
#### 3.5.2. Test Kit（应用测试服务）

##### 3.5.2.1. ArkTS API

###### 3.5.2.1.1. [@ohos.app.ability.abilityDelegatorRegistry (AbilityDelegatorRegistry)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitydelegatorregistry)
###### 3.5.2.1.2. [@ohos.application.testRunner (TestRunner)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-testrunner)
###### 3.5.2.1.3. [@ohos.UiTest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uitest)
###### 3.5.2.1.4. [@ohos.test.PerfTest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-perftest)
###### 3.5.2.1.5. 接口依赖的元素及定义

###### 3.5.2.1.5.1. [AbilityDelegator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegator)
###### 3.5.2.1.5.2. [AbilityDelegatorArgs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegatorargs)
###### 3.5.2.1.5.3. [ShellCmdResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-shellcmdresult)
###### 3.5.2.1.6. 已停止维护的接口

###### 3.5.2.1.6.1. [@ohos.application.abilityDelegatorRegistry (AbilityDelegatorRegistry)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-abilitydelegatorregistry)
##### 3.5.2.2. 错误码

###### 3.5.2.2.1. [uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)
###### 3.5.2.2.2. [perftest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-perftest)

## 4. 媒体

### 4.1. Audio Kit（音频服务）

#### 4.1.1. ArkTS API

##### 4.1.1.1. @ohos.multimedia.audio (音频管理)

###### 4.1.1.1.1. [模块描述](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio)
###### 4.1.1.1.2. [Functions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-f)
###### 4.1.1.1.3. [Interface (AudioCapturer)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiocapturer)
###### 4.1.1.1.4. [Interface (AudioManager)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiomanager)
###### 4.1.1.1.5. [Interface (AudioRenderer)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiorenderer)
###### 4.1.1.1.6. [Interface (AudioRoutingManager)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audioroutingmanager)
###### 4.1.1.1.7. [Interface (AudioSessionManager)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiosessionmanager)
###### 4.1.1.1.8. [Interface (AudioSpatializationManager)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiospatializationmanager)
###### 4.1.1.1.9. [Interface (AudioStreamManager)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiostreammanager)
###### 4.1.1.1.10. [Interface (AudioVolumeGroupManager)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumegroupmanager)
###### 4.1.1.1.11. [Interface (AudioVolumeManager)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager)
###### 4.1.1.1.12. [Interface (AudioLoopback)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audioloopback)
###### 4.1.1.1.13. [Interfaces (其他)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i)
###### 4.1.1.1.14. [Enums](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e)
###### 4.1.1.1.15. [Constants](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-c)
###### 4.1.1.1.16. [Types](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-t)
##### 4.1.1.2. [@ohos.multimedia.audioHaptic (音振协同)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-audiohaptic)
##### 4.1.1.3. [@ohos.multimedia.systemSoundManager (系统声音管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-systemsoundmanager)
##### 4.1.1.4. multimedia

###### 4.1.1.4.1. [SystemSoundPlayer (音效播放器)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-multimedia-systemsoundplayer)
#### 4.1.2. ArkTS组件

##### 4.1.2.1. [@ohos.multimedia.avVolumePanel (音量面板)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-multimedia-avvolumepanel)
#### 4.1.3. C API

##### 4.1.3.1. 模块

###### 4.1.3.1.1. [OHAudio](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio)
###### 4.1.3.1.2. [OHAudioSuite](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite)
###### 4.1.3.1.3. [AudioConverter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-audioconverter)
###### 4.1.3.1.4. [OHMIDI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohmidi)
##### 4.1.3.2. 头文件

###### 4.1.3.2.1. [native_audiocapturer.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiocapturer-h)
###### 4.1.3.2.2. [native_audio_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-manager-h)
###### 4.1.3.2.3. [native_audio_routing_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-routing-manager-h)
###### 4.1.3.2.4. [native_audio_session_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-session-manager-h)
###### 4.1.3.2.5. [native_audio_stream_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-stream-manager-h)
###### 4.1.3.2.6. [native_audio_volume_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-volume-manager-h)
###### 4.1.3.2.7. [native_audiorenderer.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiorenderer-h)
###### 4.1.3.2.8. [native_audio_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-common-h)
###### 4.1.3.2.9. [native_audio_converter.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-converter-h)
###### 4.1.3.2.10. [native_audio_device_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-device-base-h)
###### 4.1.3.2.11. [native_audio_resource_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-resource-manager-h)
###### 4.1.3.2.12. [native_audiostream_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiostream-base-h)
###### 4.1.3.2.13. [native_audiostreambuilder.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiostreambuilder-h)
###### 4.1.3.2.14. [native_audio_suite_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h)
###### 4.1.3.2.15. [native_audio_suite_engine.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-engine-h)
###### 4.1.3.2.16. [native_audio_session_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-session-base-h)
###### 4.1.3.2.17. [native_midi_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-midi-base-h)
###### 4.1.3.2.18. [native_midi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-midi-h)
##### 4.1.3.3. 结构体

###### 4.1.3.3.1. [OH_AudioManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiomanager)
###### 4.1.3.3.2. [OH_AudioRoutingManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audioroutingmanager)
###### 4.1.3.3.3. [OH_AudioSession_Strategy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiosession-strategy)
###### 4.1.3.3.4. [OH_AudioSession_DeactivatedEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiosession-deactivatedevent)
###### 4.1.3.3.5. [OH_AudioSession_StateChangedEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiosession-statechangedevent)
###### 4.1.3.3.6. [OH_AudioSessionManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiosessionmanager)
###### 4.1.3.3.7. [OH_AudioStreamManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiostreammanager)
###### 4.1.3.3.8. [OH_AudioVolumeManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiovolumemanager)
###### 4.1.3.3.9. [OH_AudioDeviceDescriptorArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiodevicedescriptorarray)
###### 4.1.3.3.10. [OH_AudioDeviceDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiodevicedescriptor)
###### 4.1.3.3.11. [OH_AudioResourceManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audioresourcemanager)
###### 4.1.3.3.12. [OH_AudioWorkgroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audioworkgroup)
###### 4.1.3.3.13. [OH_AudioStreamInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiostreaminfo)
###### 4.1.3.3.14. [OH_AudioRenderer_Callbacks_Struct](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiorenderer-callbacks-struct)
###### 4.1.3.3.15. [OH_AudioCapturer_Callbacks_Struct](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiocapturer-callbacks-struct)
###### 4.1.3.3.16. [OH_AudioStreamBuilderStruct](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiostreambuilderstruct)
###### 4.1.3.3.17. [OH_AudioRendererStruct](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiorendererstruct)
###### 4.1.3.3.18. [OH_AudioCapturerStruct](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiocapturerstruct)
###### 4.1.3.3.19. [OH_AudioFormat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite-oh-audioformat)
###### 4.1.3.3.20. [OH_AudioDataArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite-oh-audiodataarray)
###### 4.1.3.3.21. [OH_EqualizerFrequencyBandGains](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite-oh-equalizerfrequencybandgains)
###### 4.1.3.3.22. [OH_AudioSuiteEngineStruct](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite-oh-audiosuiteenginestruct)
###### 4.1.3.3.23. [OH_AudioSuitePipelineStruct](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite-oh-audiosuitepipelinestruct)
###### 4.1.3.3.24. [OH_AudioNodeStruct](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite-oh-audionodestruct)
###### 4.1.3.3.25. [OH_AudioNodeBuilderStruct](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite-oh-audionodebuilderstruct)
###### 4.1.3.3.26. [OH_AudioSuite_SpaceRenderPositionParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite-oh-audiosuite-spacerenderpositionparams)
###### 4.1.3.3.27. [OH_AudioSuite_PureVoiceChangeOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite-oh-audiosuite-purevoicechangeoption)
###### 4.1.3.3.28. [OH_AudioSuite_SpaceRenderExtensionParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite-oh-audiosuite-spacerenderextensionparams)
###### 4.1.3.3.29. [OH_AudioSuite_SpaceRenderRotationParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite-oh-audiosuite-spacerenderrotationparams)
###### 4.1.3.3.30. [OH_AudioConverter_Format](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-audioconverter-oh-audioconverter-format)
###### 4.1.3.3.31. [OH_AudioConverterStruct](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-audioconverter-oh-audioconverterstruct)
###### 4.1.3.3.32. [OH_MIDIEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohmidi-oh-midievent)
###### 4.1.3.3.33. [OH_MIDIDeviceInformation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohmidi-oh-midideviceinformation)
###### 4.1.3.3.34. [OH_MIDIPortInformation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohmidi-oh-midiportinformation)
###### 4.1.3.3.35. [OH_MIDIPortDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohmidi-oh-midiportdescriptor)
###### 4.1.3.3.36. [OH_MIDICallbacks](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohmidi-oh-midicallbacks)
###### 4.1.3.3.37. [OH_MIDIClientStruct](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohmidi-oh-midiclientstruct)
###### 4.1.3.3.38. [OH_MIDIDeviceStruct](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohmidi-oh-mididevicestruct)
#### 4.1.4. 错误码

##### 4.1.4.1. [Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)
### 4.2. AVCodec Kit（音视频编解码服务）

#### 4.2.1. C API

##### 4.2.1.1. 模块

###### 4.2.1.1.1. [AVCapability](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avcapability)
###### 4.2.1.1.2. [AudioCodec](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-audiocodec)
###### 4.2.1.1.3. [CodecBase](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-codecbase)
###### 4.2.1.1.4. [Core](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-core)
###### 4.2.1.1.5. [VideoDecoder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-videodecoder)
###### 4.2.1.1.6. [VideoEncoder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-videoencoder)
###### 4.2.1.1.7. [AVDemuxer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avdemuxer)
###### 4.2.1.1.8. [AVMuxer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmuxer)
###### 4.2.1.1.9. [AVSource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avsource)
###### 4.2.1.1.10. [Multimedia_Drm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-multimedia-drm)
##### 4.2.1.2. 头文件

###### 4.2.1.2.1. [native_avcapability.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcapability-h)
###### 4.2.1.2.2. [native_avcodec_audiocodec.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcodec-audiocodec-h)
###### 4.2.1.2.3. [native_avcodec_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcodec-base-h)
###### 4.2.1.2.4. [media_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-media-types-h)
###### 4.2.1.2.5. [native_audio_channel_layout.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h)
###### 4.2.1.2.6. [native_audio_vivid.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-vivid-h)
###### 4.2.1.2.7. [native_avbuffer.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avbuffer-h)
###### 4.2.1.2.8. [native_avbuffer_info.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avbuffer-info-h)
###### 4.2.1.2.9. [native_averrors.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-averrors-h)
###### 4.2.1.2.10. [native_avformat.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avformat-h)
###### 4.2.1.2.11. [native_avmemory.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avmemory-h)
###### 4.2.1.2.12. [native_avcodec_videodecoder.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcodec-videodecoder-h)
###### 4.2.1.2.13. [native_avcodec_videoencoder.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcodec-videoencoder-h)
###### 4.2.1.2.14. [native_avdemuxer.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avdemuxer-h)
###### 4.2.1.2.15. [native_avmuxer.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avmuxer-h)
###### 4.2.1.2.16. [native_avsource.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avsource-h)
###### 4.2.1.2.17. [native_cencinfo.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-cencinfo-h)
##### 4.2.1.3. 结构体

###### 4.2.1.3.1. [OH_AVRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avcapability-oh-avrange)
###### 4.2.1.3.2. [OH_AVCapability](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avcapability-oh-avcapability)
###### 4.2.1.3.3. [OH_AVCodecAsyncCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-codecbase-oh-avcodecasynccallback)
###### 4.2.1.3.4. [OH_AVCodecCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-codecbase-oh-avcodeccallback)
###### 4.2.1.3.5. [OH_AVDataSource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-codecbase-oh-avdatasource)
###### 4.2.1.3.6. [OH_AVDataSourceExt](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-codecbase-oh-avdatasourceext)
###### 4.2.1.3.7. [NativeWindow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-codecbase-nativewindow)
###### 4.2.1.3.8. [OH_AVCodec](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-codecbase-oh-avcodec)
###### 4.2.1.3.9. [OH_AVBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-core-oh-avbuffer)
###### 4.2.1.3.10. [OH_AVCodecBufferAttr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-core-oh-avcodecbufferattr)
###### 4.2.1.3.11. [OH_AVFormat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-core-oh-avformat)
###### 4.2.1.3.12. [OH_AVMemory](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-core-oh-avmemory)
###### 4.2.1.3.13. [OH_AVDemuxer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avdemuxer-oh-avdemuxer)
###### 4.2.1.3.14. [DRM_MediaKeySystemInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avdemuxer-drm-mediakeysysteminfo)
###### 4.2.1.3.15. [OH_AVMuxer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmuxer-oh-avmuxer)
###### 4.2.1.3.16. [OH_AVSource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avsource-oh-avsource)
###### 4.2.1.3.17. [DrmSubsample](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-multimedia-drm-drmsubsample)
###### 4.2.1.3.18. [OH_AVCencInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-multimedia-drm-oh-avcencinfo)
###### 4.2.1.3.19. [OH_CartesianPosition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-core-oh-cartesianposition)
###### 4.2.1.3.20. [OH_PolarPosition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-core-oh-polarposition)
###### 4.2.1.3.21. [OH_AudioObjectPosition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-core-oh-audioobjectposition)
###### 4.2.1.3.22. [OH_AudioVividMetaBuilderStruct](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-core-oh-audiovividmetabuilderstruct)
##### 4.2.1.4. 已停止维护的接口

###### 4.2.1.4.1. 模块

###### 4.2.1.4.1.1. [AudioDecoder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-audiodecoder)
###### 4.2.1.4.1.2. [AudioEncoder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-audioencoder)
###### 4.2.1.4.2. 头文件

###### 4.2.1.4.2.1. [avcodec_audio_channel_layout.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avcodec-audio-channel-layout-h)
###### 4.2.1.4.2.2. [native_avcodec_audiodecoder.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcodec-audiodecoder-h)
###### 4.2.1.4.2.3. [native_avcodec_audioencoder.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcodec-audioencoder-h)
### 4.3. AVSession Kit（音视频播控服务）

#### 4.3.1. ArkTS API

##### 4.3.1.1. @ohos.multimedia.avsession (媒体会话管理)

###### 4.3.1.1.1. [模块描述](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession)
###### 4.3.1.1.2. [Functions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-f)
###### 4.3.1.1.3. [Class (AVCastPickerHelper)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avcastpickerhelper)
###### 4.3.1.1.4. [Interface (AVCastController)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avcastcontroller)
###### 4.3.1.1.5. [Interface (AVSession)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsession)
###### 4.3.1.1.6. [Interface (AVSessionController)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsessioncontroller)
###### 4.3.1.1.7. [Interfaces (其他)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i)
###### 4.3.1.1.8. [Enums](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-e)
###### 4.3.1.1.9. [Types](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-t)
##### 4.3.1.2. [@ohos.multimedia.avCastPickerParam (投播组件参数)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-avcastpickerparam)
##### 4.3.1.3. @ohos.multimedia.avMusicTemplate (音频模板)

###### 4.3.1.3.1. [模块描述](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avmusictemplate)
###### 4.3.1.3.2. [Functions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avmusictemplate-f)
###### 4.3.1.3.3. [Class (AVMusicTemplate)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avmusictemplate-avmusictemplate)
###### 4.3.1.3.4. [Class (AVMusicTemplateController)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avmusictemplate-avmusictemplatecontroller)
###### 4.3.1.3.5. [Interfaces (其他)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avmusictemplate-i)
###### 4.3.1.3.6. [Enums](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avmusictemplate-e)
###### 4.3.1.3.7. [Types](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avmusictemplate-t)
#### 4.3.2. ArkTS组件

##### 4.3.2.1. [@ohos.multimedia.avCastPicker (投播组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-multimedia-avcastpicker)
##### 4.3.2.2. [@ohos.multimedia.avInputCastPicker (录音设备选择组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-multimedia-avinputcastpicker)
#### 4.3.3. C API

##### 4.3.3.1. 模块

###### 4.3.3.1.1. [OHAVSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession)
##### 4.3.3.2. 头文件

###### 4.3.3.2.1. [native_avmetadata.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avmetadata-h)
###### 4.3.3.2.2. [native_avsession.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avsession-h)
###### 4.3.3.2.3. [native_avsession_errors.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avsession-errors-h)
###### 4.3.3.2.4. [native_avcastcontroller.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcastcontroller-h)
###### 4.3.3.2.5. [native_avplaybackstate.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avplaybackstate-h)
###### 4.3.3.2.6. [native_avqueueitem.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avqueueitem-h)
###### 4.3.3.2.7. [native_avsession_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avsession-base-h)
###### 4.3.3.2.8. [native_deviceinfo.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-deviceinfo-h)
##### 4.3.3.3. 结构体

###### 4.3.3.3.1. [OH_AVMetadataBuilderStruct](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-oh-avmetadatabuilderstruct)
###### 4.3.3.3.2. [OH_AVMetadataStruct](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-oh-avmetadatastruct)
###### 4.3.3.3.3. [AVSession_PlaybackPosition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-avsession-playbackposition)
###### 4.3.3.3.4. [OH_AVSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-oh-avsession)
###### 4.3.3.3.5. [OH_AVCastController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-oh-avcastcontroller)
###### 4.3.3.3.6. [OH_AVSession_AVPlaybackState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-oh-avsession-avplaybackstate)
###### 4.3.3.3.7. [OH_AVSession_AVQueueItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-oh-avsession-avqueueitem)
###### 4.3.3.3.8. [OH_AVSession_AVMediaDescription](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-oh-avsession-avmediadescription)
###### 4.3.3.3.9. [OH_AVSession_AVMediaDescriptionBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-oh-avsession-avmediadescriptionbuilder)
###### 4.3.3.3.10. [AVSession_OutputDeviceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-avsession-outputdeviceinfo)
###### 4.3.3.3.11. [AVSession_DeviceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-avsession-deviceinfo)
#### 4.3.4. 错误码

##### 4.3.4.1. [媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)
##### 4.3.4.2. [音频模板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avmusictemplate)
### 4.4. Camera Kit（相机服务）

#### 4.4.1. ArkTS API

##### 4.4.1.1. @ohos.multimedia.camera (相机管理)

###### 4.4.1.1.1. [模块描述](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera)
###### 4.4.1.1.2. [Functions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-f)
###### 4.4.1.1.3. [Interface (Aperture)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-aperture)
###### 4.4.1.1.4. [Interface (ApertureQuery)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-aperturequery)
###### 4.4.1.1.5. [Interface (AutoDeviceSwitch)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-autodeviceswitch)
###### 4.4.1.1.6. [Interface (AutoDeviceSwitchQuery)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-autodeviceswitchquery)
###### 4.4.1.1.7. [Interface (AutoExposure)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-autoexposure)
###### 4.4.1.1.8. [Interface (AutoExposureQuery)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-autoexposurequery)
###### 4.4.1.1.9. [Interface (CameraInput)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-camerainput)
###### 4.4.1.1.10. [Interface (CameraManager)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-cameramanager)
###### 4.4.1.1.11. [Interface (CameraOutput)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-cameraoutput)
###### 4.4.1.1.12. [Interface (CapturePhoto)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-capturephoto)
###### 4.4.1.1.13. [Interface (ColorManagement)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-colormanagement)
###### 4.4.1.1.14. [Interface (ColorManagementQuery)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-colormanagementquery)
###### 4.4.1.1.15. [Interface (ControlCenter)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-controlcenter)
###### 4.4.1.1.16. [Interface (ControlCenterQuery)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-controlcenterquery)
###### 4.4.1.1.17. [Interface (Flash)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-flash)
###### 4.4.1.1.18. [Interface (FlashQuery)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-flashquery)
###### 4.4.1.1.19. [Interface (Focus)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-focus)
###### 4.4.1.1.20. [Interface (FocusQuery)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-focusquery)
###### 4.4.1.1.21. [Interface (Macro)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-macro)
###### 4.4.1.1.22. [Interface (MacroQuery)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-macroquery)
###### 4.4.1.1.23. [Interface (ManualExposure)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-manualexposure)
###### 4.4.1.1.24. [Interface (ManualExposureQuery)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-manualexposurequery)
###### 4.4.1.1.25. [Interface (ManualFocus)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-manualfocus)
###### 4.4.1.1.26. [Interface (ManualFocusQuery)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-manualfocusquery)
###### 4.4.1.1.27. [Interface (ManualIso)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-manualiso)
###### 4.4.1.1.28. [Interface (ManualIsoQuery)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-manualisoquery)
###### 4.4.1.1.29. [Interface (MetadataOutput)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-metadataoutput)
###### 4.4.1.1.30. [Interface (OIS)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-ois)
###### 4.4.1.1.31. [Interface (OISQuery)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-oisquery)
###### 4.4.1.1.32. [Interface (Photo)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-photo)
###### 4.4.1.1.33. [Interface (PhotoOutput)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-photooutput)
###### 4.4.1.1.34. [Interface (PhotoSession)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-photosession)
###### 4.4.1.1.35. [Interface (PreviewOutput)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-previewoutput)
###### 4.4.1.1.36. [Interface (SecureSession)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-securesession)
###### 4.4.1.1.37. [Interface (Session)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-session)
###### 4.4.1.1.38. [Interface (Stabilization)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-stabilization)
###### 4.4.1.1.39. [Interface (StabilizationQuery)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-stabilizationquery)
###### 4.4.1.1.40. [Interface (VideoOutput)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-videooutput)
###### 4.4.1.1.41. [Interface (VideoSession)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-videosession)
###### 4.4.1.1.42. [Interface (WhiteBalance)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-whitebalance)
###### 4.4.1.1.43. [Interface (WhiteBalanceQuery)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-whitebalancequery)
###### 4.4.1.1.44. [Interface (Zoom)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-zoom)
###### 4.4.1.1.45. [Interface (ZoomQuery)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-zoomquery)
###### 4.4.1.1.46. [Interfaces (其他)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-i)
###### 4.4.1.1.47. [Enums](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-e)
###### 4.4.1.1.48. [Types](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-t)
###### 4.4.1.1.49. [废弃的Interface (CaptureSession, deprecated)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-capturesession)
##### 4.4.1.2. [@ohos.multimedia.cameraPicker (相机选择器)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-camerapicker)
#### 4.4.2. C API

##### 4.4.2.1. 模块

###### 4.4.2.1.1. [OH_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)
##### 4.4.2.2. 头文件

###### 4.4.2.2.1. [camera.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h)
###### 4.4.2.2.2. [camera_device.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-device-h)
###### 4.4.2.2.3. [camera_input.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-input-h)
###### 4.4.2.2.4. [camera_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h)
###### 4.4.2.2.5. [capture_session.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h)
###### 4.4.2.2.6. [metadata_output.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-metadata-output-h)
###### 4.4.2.2.7. [photo_native.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-photo-native-h)
###### 4.4.2.2.8. [photo_output.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-photo-output-h)
###### 4.4.2.2.9. [preview_output.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-preview-output-h)
###### 4.4.2.2.10. [video_output.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-output-h)
##### 4.4.2.3. 结构体

###### 4.4.2.3.1. [Camera_Size](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-size)
###### 4.4.2.3.2. [Camera_Profile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-profile)
###### 4.4.2.3.3. [Camera_FrameRateRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-frameraterange)
###### 4.4.2.3.4. [Camera_VideoProfile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-videoprofile)
###### 4.4.2.3.5. [Camera_OutputCapability](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-outputcapability)
###### 4.4.2.3.6. [Camera_Device](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-device)
###### 4.4.2.3.7. [Camera_DeviceQueryInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-devicequeryinfo)
###### 4.4.2.3.8. [Camera_StatusInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-statusinfo)
###### 4.4.2.3.9. [Camera_Point](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-point)
###### 4.4.2.3.10. [Camera_Location](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-location)
###### 4.4.2.3.11. [Camera_PhotoCaptureSetting](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-photocapturesetting)
###### 4.4.2.3.12. [Camera_FrameShutterInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-frameshutterinfo)
###### 4.4.2.3.13. [Camera_CaptureEndInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-captureendinfo)
###### 4.4.2.3.14. [Camera_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-rect)
###### 4.4.2.3.15. [Camera_MetadataObject](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-metadataobject)
###### 4.4.2.3.16. [Camera_TorchStatusInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-torchstatusinfo)
###### 4.4.2.3.17. [Camera_SmoothZoomInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-smoothzoominfo)
###### 4.4.2.3.18. [Camera_CaptureStartInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-capturestartinfo)
###### 4.4.2.3.19. [Camera_FrameShutterEndInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-frameshutterendinfo)
###### 4.4.2.3.20. [Camera_FoldStatusInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-foldstatusinfo)
###### 4.4.2.3.21. [Camera_AutoDeviceSwitchStatusInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-autodeviceswitchstatusinfo)
###### 4.4.2.3.22. [Camera_ConcurrentInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-concurrentinfo)
###### 4.4.2.3.23. [Camera_ControlCenterStatusInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-controlcenterstatusinfo)
###### 4.4.2.3.24. [Camera_Manager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-manager)
###### 4.4.2.3.25. [CameraInput_Callbacks](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camerainput-callbacks)
###### 4.4.2.3.26. [Camera_Input](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-input)
###### 4.4.2.3.27. [CameraManager_Callbacks](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-cameramanager-callbacks)
###### 4.4.2.3.28. [CaptureSession_Callbacks](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-capturesession-callbacks)
###### 4.4.2.3.29. [Camera_CaptureSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-capturesession)
###### 4.4.2.3.30. [MetadataOutput_Callbacks](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-metadataoutput-callbacks)
###### 4.4.2.3.31. [Camera_MetadataOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-metadataoutput)
###### 4.4.2.3.32. [OH_PhotoNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-oh-photonative)
###### 4.4.2.3.33. [PhotoOutput_Callbacks](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-photooutput-callbacks)
###### 4.4.2.3.34. [Camera_PhotoOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-photooutput)
###### 4.4.2.3.35. [PreviewOutput_Callbacks](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-previewoutput-callbacks)
###### 4.4.2.3.36. [Camera_PreviewOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-previewoutput)
###### 4.4.2.3.37. [VideoOutput_Callbacks](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-videooutput-callbacks)
###### 4.4.2.3.38. [Camera_VideoOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-videooutput)
###### 4.4.2.3.39. [Camera_OcclusionDetectionResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-occlusiondetectionresult)
###### 4.4.2.3.40. [OH_Camera_ZoomRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-oh-camera-zoomrange)
###### 4.4.2.3.41. [OH_Camera_PhysicalAperture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-oh-camera-physicalaperture)
###### 4.4.2.3.42. [OH_Camera_ZoomPointInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-oh-camera-zoompointinfo)
#### 4.4.3. 错误码

##### 4.4.3.1. [Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)
### 4.5. DRM Kit（数字版权保护服务）

#### 4.5.1. ArkTS API

##### 4.5.1.1. @ohos.multimedia.drm (数字版权保护)

###### 4.5.1.1.1. [模块描述](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-drm)
###### 4.5.1.1.2. [Functions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-drm-f)
###### 4.5.1.1.3. [Interface (MediaKeySession)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-drm-mediakeysession)
###### 4.5.1.1.4. [Interface (MediaKeySystem)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-drm-mediakeysystem)
###### 4.5.1.1.5. [Interfaces (其他)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-drm-i)
###### 4.5.1.1.6. [Enums](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-drm-e)
#### 4.5.2. C API

##### 4.5.2.1. 模块

###### 4.5.2.1.1. [Drm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm)
##### 4.5.2.2. 头文件

###### 4.5.2.2.1. [native_drm_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-common-h)
###### 4.5.2.2.2. [native_drm_err.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-err-h)
###### 4.5.2.2.3. [native_mediakeysession.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-mediakeysession-h)
###### 4.5.2.2.4. [native_mediakeysystem.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-mediakeysystem-h)
##### 4.5.2.3. 结构体

###### 4.5.2.3.1. [DRM_MediaKeyRequestInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-mediakeyrequestinfo)
###### 4.5.2.3.2. [DRM_MediaKeyRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-mediakeyrequest)
###### 4.5.2.3.3. [DRM_Statistics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-statistics)
###### 4.5.2.3.4. [DRM_OfflineMediakeyIdArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-offlinemediakeyidarray)
###### 4.5.2.3.5. [DRM_KeysInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-keysinfo)
###### 4.5.2.3.6. [DRM_MediaKeyStatus](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-mediakeystatus)
###### 4.5.2.3.7. [DRM_PsshInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-psshinfo)
###### 4.5.2.3.8. [DRM_MediaKeySystemInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-mediakeysysteminfo)
###### 4.5.2.3.9. [DRM_MediaKeySystemDescription](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-mediakeysystemdescription)
###### 4.5.2.3.10. [MediaKeySystem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-mediakeysystem)
###### 4.5.2.3.11. [MediaKeySession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-mediakeysession)
###### 4.5.2.3.12. [MediaKeySession_Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-mediakeysession-callback)
###### 4.5.2.3.13. [OH_MediaKeySession_Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-oh-mediakeysession-callback)
#### 4.5.3. 错误码

##### 4.5.3.1. [DRM错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-drm)
### 4.6. Image Kit（图片处理服务）

#### 4.6.1. ArkTS API

##### 4.6.1.1. @ohos.multimedia.image (图片处理)

###### 4.6.1.1.1. [模块描述](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image)
###### 4.6.1.1.2. [Functions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-f)
###### 4.6.1.1.3. [Interface (AuxiliaryPicture)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-auxiliarypicture)
###### 4.6.1.1.4. [Interface (Image)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-image)
###### 4.6.1.1.5. [Interface (ImageCreator)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagecreator)
###### 4.6.1.1.6. [Interface (ImagePacker)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagepacker)
###### 4.6.1.1.7. [Interface (ImageReceiver)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagereceiver)
###### 4.6.1.1.8. [Interface (ImageSource)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagesource)
###### 4.6.1.1.9. [Interface (Metadata)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-metadata)
###### 4.6.1.1.10. [Class (ExifMetadata)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-exifmetadata)
###### 4.6.1.1.11. [Class (MakerNoteHuaweiMetadata)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-makernotehuaweimetadata)
###### 4.6.1.1.12. [Class (HeifsMetadata)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-heifsmetadata)
###### 4.6.1.1.13. [Class (WebPMetadata)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-webpmetadata)
###### 4.6.1.1.14. [Class (GifMetadata)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-gifmetadata)
###### 4.6.1.1.15. [Class (JfifMetadata)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-jfifmetadata)
###### 4.6.1.1.16. [Class (TiffMetadata)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-tiffmetadata)
###### 4.6.1.1.17. [Class (PngMetadata)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pngmetadata)
###### 4.6.1.1.18. [Class (XMPMetadata)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-xmpmetadata)
###### 4.6.1.1.19. [Class (AvisMetadata)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-avismetadata)
###### 4.6.1.1.20. [Interface (Picture)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-picture)
###### 4.6.1.1.21. [Interface (PixelMap)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)
###### 4.6.1.1.22. [Interfaces (其他)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-i)
###### 4.6.1.1.23. [Enums](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-e)
###### 4.6.1.1.24. [Types](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-t)
###### 4.6.1.1.25. [Constants](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-c)
##### 4.6.1.2. [@ohos.multimedia.sendableImage (基于Sendable对象的图片处理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sendableimage)
##### 4.6.1.3. [@ohos.multimedia.videoProcessingEngine (视频处理引擎)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-videoprocessingengine)
#### 4.6.2. C API

##### 4.6.2.1. 模块

###### 4.6.2.1.1. [Image_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)
###### 4.6.2.1.2. [Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image)
###### 4.6.2.1.3. [ImageEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageeffect)
###### 4.6.2.1.4. [ImageProcessing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageprocessing)
##### 4.6.2.2. 头文件

###### 4.6.2.2.1. [image_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-common-h)
###### 4.6.2.2.2. [image_native.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-native-h)
###### 4.6.2.2.3. [image_packer_native.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-packer-native-h)
###### 4.6.2.2.4. [image_receiver_native.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-receiver-native-h)
###### 4.6.2.2.5. [image_source_native.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-native-h)
###### 4.6.2.2.6. [picture_native.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-picture-native-h)
###### 4.6.2.2.7. [pixelmap_native.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h)
###### 4.6.2.2.8. [image_mdk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-mdk-h)
###### 4.6.2.2.9. [image_mdk_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-mdk-common-h)
###### 4.6.2.2.10. [image_packer_mdk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-packer-mdk-h)
###### 4.6.2.2.11. [image_pixel_map_mdk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-pixel-map-mdk-h)
###### 4.6.2.2.12. [image_pixel_map_napi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-pixel-map-napi-h)
###### 4.6.2.2.13. [image_receiver_mdk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-receiver-mdk-h)
###### 4.6.2.2.14. [image_source_mdk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h)
###### 4.6.2.2.15. [image_effect.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-effect-h)
###### 4.6.2.2.16. [image_effect_errors.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-effect-errors-h)
###### 4.6.2.2.17. [image_effect_filter.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-effect-filter-h)
###### 4.6.2.2.18. [image_processing.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-processing-h)
###### 4.6.2.2.19. [image_processing_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-processing-types-h)
##### 4.6.2.3. 结构体

###### 4.6.2.3.1. [OH_ImageSourceNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-imagesourcenative)
###### 4.6.2.3.2. [OH_ImageSource_Info](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-imagesource-info)
###### 4.6.2.3.3. [OH_DecodingOptionsForPicture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-decodingoptionsforpicture)
###### 4.6.2.3.4. [OH_DecodingOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-decodingoptions)
###### 4.6.2.3.5. [OH_PixelmapNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-pixelmapnative)
###### 4.6.2.3.6. [OH_NativeBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-image-nativemodule-oh-nativebuffer)
###### 4.6.2.3.7. [OH_Pixelmap_HdrStaticMetadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-pixelmap-hdrstaticmetadata)
###### 4.6.2.3.8. [OH_NativeColorSpaceManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-nativecolorspacemanager)
###### 4.6.2.3.9. [OH_Pixelmap_HdrDynamicMetadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-pixelmap-hdrdynamicmetadata)
###### 4.6.2.3.10. [OH_Pixelmap_HdrGainmapMetadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-pixelmap-hdrgainmapmetadata)
###### 4.6.2.3.11. [OH_Pixelmap_HdrMetadataValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-pixelmap-hdrmetadatavalue)
###### 4.6.2.3.12. [OH_Pixelmap_InitializationOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-pixelmap-initializationoptions)
###### 4.6.2.3.13. [OH_Pixelmap_ImageInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-pixelmap-imageinfo)
###### 4.6.2.3.14. [Image_Size](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-image-size)
###### 4.6.2.3.15. [Image_Region](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-image-region)
###### 4.6.2.3.16. [OH_PictureMetadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-picturemetadata)
###### 4.6.2.3.17. [Image_String](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-image-string)
###### 4.6.2.3.18. [OH_ImageNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-imagenative)
###### 4.6.2.3.19. [OH_ImagePackerNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-imagepackernative)
###### 4.6.2.3.20. [OH_ImageBufferData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-imagebufferdata)
###### 4.6.2.3.21. [OH_PackingOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-packingoptions)
###### 4.6.2.3.22. [OH_PackingOptionsForSequence](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-packingoptionsforsequence)
###### 4.6.2.3.23. [OH_ImageReceiverNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-imagereceivernative)
###### 4.6.2.3.24. [OH_ImageReceiverOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-imagereceiveroptions)
###### 4.6.2.3.25. [OH_PictureNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-picturenative)
###### 4.6.2.3.26. [OH_AuxiliaryPictureNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-auxiliarypicturenative)
###### 4.6.2.3.27. [OH_AuxiliaryPictureInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-auxiliarypictureinfo)
###### 4.6.2.3.28. [OhosImageRect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagerect)
###### 4.6.2.3.29. [ImageNative_](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagenative-)
###### 4.6.2.3.30. [OhosImageComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagecomponent)
###### 4.6.2.3.31. [OhosImageSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesize)
###### 4.6.2.3.32. [ImagePacker_Opts_](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagepacker-opts-)
###### 4.6.2.3.33. [ImagePacker_Native_](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagepacker-native-)
###### 4.6.2.3.34. [OhosPixelMapInfos](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohospixelmapinfos)
###### 4.6.2.3.35. [NativePixelMap_](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativepixelmap-)
###### 4.6.2.3.36. [OhosPixelMapCreateOps](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohospixelmapcreateops)
###### 4.6.2.3.37. [OhosPixelMapInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohospixelmapinfo)
###### 4.6.2.3.38. [OhosImageReceiverInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagereceiverinfo)
###### 4.6.2.3.39. [ImageReceiverNative_](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-)
###### 4.6.2.3.40. [OhosImageRegion](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimageregion)
###### 4.6.2.3.41. [ImageSourceNative_](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagesourcenative-)
###### 4.6.2.3.42. [OhosImageSourceOps](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourceops)
###### 4.6.2.3.43. [OhosImageDecodingOps](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagedecodingops)
###### 4.6.2.3.44. [OhosImageSourceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourceinfo)
###### 4.6.2.3.45. [OhosImageSource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesource)
###### 4.6.2.3.46. [OhosImageSourceDelayTimeList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourcedelaytimelist)
###### 4.6.2.3.47. [OhosImageSourceSupportedFormat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourcesupportedformat)
###### 4.6.2.3.48. [OhosImageSourceSupportedFormatList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourcesupportedformatlist)
###### 4.6.2.3.49. [OhosImageSourceProperty](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourceproperty)
###### 4.6.2.3.50. [OhosImageSourceUpdateData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourceupdatedata)
###### 4.6.2.3.51. [OH_ImageEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageeffect-oh-imageeffect)
###### 4.6.2.3.52. [ImageEffect_DataValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageeffect-imageeffect-datavalue)
###### 4.6.2.3.53. [OH_EffectFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageeffect-oh-effectfilter)
###### 4.6.2.3.54. [OH_EffectFilterInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageeffect-oh-effectfilterinfo)
###### 4.6.2.3.55. [OH_EffectBufferInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageeffect-oh-effectbufferinfo)
###### 4.6.2.3.56. [ImageEffect_Any](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageeffect-imageeffect-any)
###### 4.6.2.3.57. [ImageEffect_FilterNames](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageeffect-imageeffect-filternames)
###### 4.6.2.3.58. [ImageEffect_FilterDelegate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageeffect-imageeffect-filterdelegate)
###### 4.6.2.3.59. [ImageEffect_Region](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageeffect-imageeffect-region)
###### 4.6.2.3.60. [ImageEffect_Size](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageeffect-imageeffect-size)
###### 4.6.2.3.61. [ImageProcessing_ColorSpaceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageprocessing-imageprocessing-colorspaceinfo)
###### 4.6.2.3.62. [OH_ImageProcessing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageprocessing-oh-imageprocessing)
###### 4.6.2.3.63. [Image_PositionArea](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-image-positionarea)
###### 4.6.2.3.64. [Image_Scale](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-image-scale)
###### 4.6.2.3.65. [OH_ComposeOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-composeoptions)
###### 4.6.2.3.66. [OH_ImageRawData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-imagerawdata)
#### 4.6.3. 错误码

##### 4.6.3.1. [Image错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-image)
##### 4.6.3.2. [视频处理引擎错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-videoprocessingengine)
### 4.7. Media Kit（媒体服务）

#### 4.7.1. ArkTS API

##### 4.7.1.1. @ohos.multimedia.media (媒体服务)

###### 4.7.1.1.1. [模块描述](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media)
###### 4.7.1.1.2. [Functions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-f)
###### 4.7.1.1.3. [Interface (AVImageGenerator)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avimagegenerator)
###### 4.7.1.1.4. [Interface (AVMetadataExtractor)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avmetadataextractor)
###### 4.7.1.1.5. [Interface (AVPlayer)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer)
###### 4.7.1.1.6. [Interface (AVRecorder)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avrecorder)
###### 4.7.1.1.7. [Interface (AVScreenCaptureRecorder)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avscreencapturerecorder)
###### 4.7.1.1.8. [Interface (AVTranscoder)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avtranscoder)
###### 4.7.1.1.9. [Interface (MediaSource)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-mediasource)
###### 4.7.1.1.10. [Interface (MediaSourceLoadingRequest)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-mediasourceloadingrequest)
###### 4.7.1.1.11. [Interfaces (其他)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-i)
###### 4.7.1.1.12. [Enums](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-e)
###### 4.7.1.1.13. [Types](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-t)
###### 4.7.1.1.14. [废弃的Interface (AudioPlayer, deprecated)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-audioplayer)
###### 4.7.1.1.15. [废弃的Interface (AudioRecorder, deprecated)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-audiorecorder)
###### 4.7.1.1.16. [废弃的Interface (VideoPlayer, deprecated)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-videoplayer)
##### 4.7.1.2. multimedia

###### 4.7.1.2.1. [SoundPool (音频池)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-multimedia-soundpool)
#### 4.7.2. C API

##### 4.7.2.1. 模块

###### 4.7.2.1.1. [AVImageGenerator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avimagegenerator)
###### 4.7.2.1.2. [AVMetadataExtractor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmetadataextractor)
###### 4.7.2.1.3. [AVPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer)
###### 4.7.2.1.4. [AVRecorder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder)
###### 4.7.2.1.5. [AVTranscoder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avtranscoder)
###### 4.7.2.1.6. [AVScreenCapture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture)
###### 4.7.2.1.7. [AVSinkBase](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avsinkbase)
###### 4.7.2.1.8. [LowPowerAudioSink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-lowpoweraudiosink)
###### 4.7.2.1.9. [LowPowerVideoSink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-lowpowervideosink)
###### 4.7.2.1.10. [VideoProcessing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-videoprocessing)
###### 4.7.2.1.11. [AVMediaSource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmedia-source)
###### 4.7.2.1.12. [AVMediaBase](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmediabase)
##### 4.7.2.2. 头文件

###### 4.7.2.2.1. [avimage_generator.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avimage-generator-h)
###### 4.7.2.2.2. [avimage_generator_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avimage-generator-base-h)
###### 4.7.2.2.3. [avmetadata_extractor.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmetadata-extractor-h)
###### 4.7.2.2.4. [avmetadata_extractor_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmetadata-extractor-base-h)
###### 4.7.2.2.5. [avplayer.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-h)
###### 4.7.2.2.6. [avplayer_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-base-h)
###### 4.7.2.2.7. [avrecorder.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-h)
###### 4.7.2.2.8. [avrecorder_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-base-h)
###### 4.7.2.2.9. [avtranscoder.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avtranscoder-h)
###### 4.7.2.2.10. [avtranscoder_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avtranscoder-base-h)
###### 4.7.2.2.11. [native_avscreen_capture.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-h)
###### 4.7.2.2.12. [native_avscreen_capture_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h)
###### 4.7.2.2.13. [native_avscreen_capture_errors.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-errors-h)
###### 4.7.2.2.14. [lowpower_audio_sink.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-lowpower-audio-sink-h)
###### 4.7.2.2.15. [lowpower_audio_sink_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-lowpower-audio-sink-base-h)
###### 4.7.2.2.16. [lowpower_avsink_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-lowpower-avsink-base-h)
###### 4.7.2.2.17. [lowpower_video_sink.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-lowpower-video-sink-h)
###### 4.7.2.2.18. [lowpower_video_sink_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-lowpower-video-sink-base-h)
###### 4.7.2.2.19. [video_processing.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-processing-h)
###### 4.7.2.2.20. [video_processing_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-processing-types-h)
###### 4.7.2.2.21. [avmedia_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmedia-base-h)
###### 4.7.2.2.22. [avmedia_source.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmedia-source-h)
###### 4.7.2.2.23. [avmetakeys.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmetakeys-h)
##### 4.7.2.3. 结构体

###### 4.7.2.3.1. [OH_AVImageGenerator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avimagegenerator-oh-avimagegenerator)
###### 4.7.2.3.2. [OH_AVMetadataExtractor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmetadataextractor-oh-avmetadataextractor)
###### 4.7.2.3.3. [MediaKeySession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-mediakeysession)
###### 4.7.2.3.4. [DRM_MediaKeySystemInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-drm-mediakeysysteminfo)
###### 4.7.2.3.5. [AVPlayerCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-avplayercallback)
###### 4.7.2.3.6. [OH_AVPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-oh-avplayer)
###### 4.7.2.3.7. [OH_AVRecorder_Profile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-profile)
###### 4.7.2.3.8. [OH_AVRecorder_Location](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-location)
###### 4.7.2.3.9. [OH_AVRecorder_MetadataTemplate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-metadatatemplate)
###### 4.7.2.3.10. [OH_AVRecorder_Metadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-metadata)
###### 4.7.2.3.11. [OH_AVRecorder_Config](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-config)
###### 4.7.2.3.12. [OH_AVRecorder_Range](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-range)
###### 4.7.2.3.13. [OH_AVRecorder_EncoderInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-encoderinfo)
###### 4.7.2.3.14. [OH_AVRecorder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder)
###### 4.7.2.3.15. [OH_AVTranscoder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avtranscoder-oh-avtranscoder)
###### 4.7.2.3.16. [OH_AVTranscoder_Config](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avtranscoder-oh-avtranscoder-config)
###### 4.7.2.3.17. [OH_AudioCaptureInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-audiocaptureinfo)
###### 4.7.2.3.18. [OH_AudioEncInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-audioencinfo)
###### 4.7.2.3.19. [OH_AudioInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-audioinfo)
###### 4.7.2.3.20. [OH_VideoCaptureInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-videocaptureinfo)
###### 4.7.2.3.21. [OH_VideoEncInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-videoencinfo)
###### 4.7.2.3.22. [OH_VideoInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-videoinfo)
###### 4.7.2.3.23. [OH_RecorderInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-recorderinfo)
###### 4.7.2.3.24. [OH_AVScreenCaptureConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-avscreencaptureconfig)
###### 4.7.2.3.25. [OH_PrivacyProtectInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-privacyprotectinfo)
###### 4.7.2.3.26. [OH_AVScreenCaptureCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-avscreencapturecallback)
###### 4.7.2.3.27. [OH_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-rect)
###### 4.7.2.3.28. [OH_AudioBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-audiobuffer)
###### 4.7.2.3.29. [OH_NativeBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-avscreencapture-oh-nativebuffer)
###### 4.7.2.3.30. [OH_AVScreenCapture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-avscreencapture)
###### 4.7.2.3.31. [OH_AVScreenCapture_ContentFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-avscreencapture-contentfilter)
###### 4.7.2.3.32. [OH_AVScreenCapture_CaptureStrategy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-avscreencapture-capturestrategy)
###### 4.7.2.3.33. [OH_AVScreenCapture_UserSelectionInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-avscreencapture-userselectioninfo)
###### 4.7.2.3.34. [OH_AVScreenCaptureHighlightConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-avscreencapturehighlightconfig)
###### 4.7.2.3.35. [OH_LowPowerAudioSink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-lowpoweraudiosink-oh-lowpoweraudiosink)
###### 4.7.2.3.36. [OH_LowPowerAudioSinkCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-lowpoweraudiosink-oh-lowpoweraudiosinkcallback)
###### 4.7.2.3.37. [OH_AVSamplesBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avsinkbase-oh-avsamplesbuffer)
###### 4.7.2.3.38. [OH_LowPowerVideoSink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-lowpowervideosink-oh-lowpowervideosink)
###### 4.7.2.3.39. [OH_LowPowerVideoSinkCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-lowpowervideosink-oh-lowpowervideosinkcallback)
###### 4.7.2.3.40. [VideoProcessing_ColorSpaceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-videoprocessing-videoprocessing-colorspaceinfo)
###### 4.7.2.3.41. [OH_VideoProcessing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-videoprocessing-oh-videoprocessing)
###### 4.7.2.3.42. [NativeWindow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-videoprocessing-nativewindow)
###### 4.7.2.3.43. [OH_AVFormat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-videoprocessing-oh-avformat)
###### 4.7.2.3.44. [VideoProcessing_Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-videoprocessing-videoprocessing-callback)
###### 4.7.2.3.45. [OH_AVPlaybackStrategy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-oh-avplaybackstrategy)
###### 4.7.2.3.46. [OH_AVMediaSource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmedia-source-oh-avmediasource)
###### 4.7.2.3.47. [OH_AVHttpHeader](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmedia-source-oh-avhttpheader)
###### 4.7.2.3.48. [OH_AVMediaSourceLoadingRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmedia-source-oh-avmediasourceloadingrequest)
###### 4.7.2.3.49. [OH_AVMediaSourceLoader](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmedia-source-oh-avmediasourceloader)
###### 4.7.2.3.50. [OH_AVSeiMessageArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-oh-avseimessagearray)
###### 4.7.2.3.51. [OH_AVMetadataExtractor_OutputParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmetadataextractor-oh-avmetadataextractor-outputparam)
###### 4.7.2.3.52. [OH_AVMetadataExtractor_FrameInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmetadataextractor-oh-avmetadataextractor-frameinfo)
###### 4.7.2.3.53. [OH_MultiDisplayCapability](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-multidisplaycapability)
###### 4.7.2.3.54. [OH_AVPlayerVideoOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-oh-avplayervideooutput)
#### 4.7.3. 错误码

##### 4.7.3.1. [Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)
### 4.8. Media Library Kit（媒体文件管理服务）

#### 4.8.1. ArkTS API

##### 4.8.1.1. @ohos.file.photoAccessHelper (相册管理模块)

###### 4.8.1.1.1. [模块描述](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper)
###### 4.8.1.1.2. [Functions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-f)
###### 4.8.1.1.3. [Class (MediaAlbumChangeRequest)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-mediaalbumchangerequest)
###### 4.8.1.1.4. [Class (MediaAssetChangeRequest)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-mediaassetchangerequest)
###### 4.8.1.1.5. [Class (MediaAssetManager)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-mediaassetmanager)
###### 4.8.1.1.6. [Class (PhotoViewPicker)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker)
###### 4.8.1.1.7. [Classes (其他)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-class)
###### 4.8.1.1.8. [Interface (AbsAlbum)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-absalbum)
###### 4.8.1.1.9. [Interface (Album)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-album)
###### 4.8.1.1.10. [Interface (FetchResult)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-fetchresult)
###### 4.8.1.1.11. [Interface (MediaAssetDataHandler)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-mediaassetdatahandler)
###### 4.8.1.1.12. [Interface (MediaAssetProgressHandler)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-mediaassetprogresshandler)
###### 4.8.1.1.13. [Interface (MovingPhoto)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-movingphoto)
###### 4.8.1.1.14. [Interface (PhotoAccessHelper)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper)
###### 4.8.1.1.15. [Interface (PhotoAsset)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoasset)
###### 4.8.1.1.16. [Interface (QuickImageDataHandler)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-quickimagedatahandler)
###### 4.8.1.1.17. [Interfaces (其他)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-i)
###### 4.8.1.1.18. [Enums](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-e)
###### 4.8.1.1.19. [Types](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-t)
##### 4.8.1.2. [@ohos.file.sendablePhotoAccessHelper (基于Sendable对象的相册管理模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sendablephotoaccesshelper)
#### 4.8.2. ArkTS组件

##### 4.8.2.1. [@ohos.file.AlbumPickerComponent (Album Picker组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-file-albumpickercomponent)
##### 4.8.2.2. [@ohos.file.PhotoPickerComponent (PhotoPicker组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-file-photopickercomponent)
##### 4.8.2.3. [@ohos.file.RecentPhotoComponent (最近图片组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-file-recentphotocomponent)
##### 4.8.2.4. [@ohos.multimedia.movingphotoview (动态照片)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-multimedia-movingphotoview)
#### 4.8.3. C API

##### 4.8.3.1. 模块

###### 4.8.3.1.1. [MediaAssetManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager)
##### 4.8.3.2. 头文件

###### 4.8.3.2.1. [media_access_helper_capi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-media-access-helper-capi-h)
###### 4.8.3.2.2. [media_asset_base_capi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-media-asset-base-capi-h)
###### 4.8.3.2.3. [media_asset_capi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-media-asset-capi-h)
###### 4.8.3.2.4. [media_asset_change_request_capi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-media-asset-change-request-capi-h)
###### 4.8.3.2.5. [media_asset_manager_capi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-media-asset-manager-capi-h)
###### 4.8.3.2.6. [moving_photo_capi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-moving-photo-capi-h)
##### 4.8.3.3. 结构体

###### 4.8.3.3.1. [MediaLibrary_RequestId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager-medialibrary-requestid)
###### 4.8.3.3.2. [OH_MediaAssetManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager-oh-mediaassetmanager)
###### 4.8.3.3.3. [OH_MediaAssetChangeRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager-oh-mediaassetchangerequest)
###### 4.8.3.3.4. [OH_MovingPhoto](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager-oh-movingphoto)
###### 4.8.3.3.5. [OH_MediaAsset](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager-oh-mediaasset)
###### 4.8.3.3.6. [MediaLibrary_RequestOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager-medialibrary-requestoptions)
#### 4.8.4. 错误码

##### 4.8.4.1. [媒体库错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-medialibrary)
### 4.9. Ringtone Kit（铃声服务）

#### 4.9.1. ArkTS API

##### 4.9.1.1. [ringtone（铃声服务）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ringtone-ringtone)
##### 4.9.1.2. [ArkTS API 错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-ringtone)
### 4.10. Scan Kit（统一扫码服务）

#### 4.10.1. ArkTS API

##### 4.10.1.1. [customScan (自定义界面扫码)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan-customscan-api)
##### 4.10.1.2. [detectBarcode (图像识码)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan-imagedecode)
##### 4.10.1.3. [generateBarcode (码图生成)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan-generatebarcode)
##### 4.10.1.4. [scanBarcode (默认界面扫码)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan-scanbarcode-api)
##### 4.10.1.5. [scanCore (扫码公共信息)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan-scancore)
##### 4.10.1.6. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-scan)

## 5. 图形

### 5.1. AR Engine（AR引擎服务）

#### 5.1.1. ArkTS API

##### 5.1.1.1. [arEngine（AR增强现实能力）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-arengine)
##### 5.1.1.2. [arViewController（AR场景管理能力）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-arviewcontroller)
#### 5.1.2. ArkTS组件

##### 5.1.2.1. [ARView（AR场景可视化）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-component-arview)
#### 5.1.3. C API

##### 5.1.3.1. 模块

###### 5.1.3.1.1. [AR Engine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine)
##### 5.1.3.2. 头文件和结构体

###### 5.1.3.2.1. 头文件

###### 5.1.3.2.1.1. [ar_engine_core.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-header-file)
###### 5.1.3.2.2. 结构体

###### 5.1.3.2.2.1. [AREngine_ARAugmentedImageSource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-struct-araugmentedimagesource)
###### 5.1.3.2.2.2. [AREngine_ClipPlaneDistance](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-struct-clipplanedistance)
###### 5.1.3.2.2.3. [AREngine_ARSemanticDensePointData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-struct-arsemanticdensepointdata)
###### 5.1.3.2.2.4. [AREngine_ARSemanticDenseCubeData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-struct-arsemanticdensecubedata)
#### 5.1.4. [AR Engine错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-ar-engine)
### 5.2. ArkGraphics 2D（方舟2D图形服务）

#### 5.2.1. ArkTS API

##### 5.2.1.1. [@ohos.effectKit (图像效果)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-effectkit)
##### 5.2.1.2. [@ohos.graphics.colorSpaceManager (色彩管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-colorspacemanager)
##### 5.2.1.3. [@ohos.graphics.sendableColorSpaceManager (可共享的色彩管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sendablecolorspacemanager)
##### 5.2.1.4. [@ohos.graphics.common2D (2D图形通用数据类型)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-graphics-common2d)
##### 5.2.1.5. [@ohos.graphics.displaySync (可变帧率)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-graphics-displaysync)
##### 5.2.1.6. @ohos.graphics.drawing (绘制模块)

###### 5.2.1.6.1. [模块描述](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing)
###### 5.2.1.6.2. [Class (Brush)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-brush)
###### 5.2.1.6.3. [Class (Canvas)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-canvas)
###### 5.2.1.6.4. [Class (ColorFilter)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-colorfilter)
###### 5.2.1.6.5. [Class (Font)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-font)
###### 5.2.1.6.6. [Class (ImageFilter)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-imagefilter)
###### 5.2.1.6.7. [Class (Lattice)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-lattice)
###### 5.2.1.6.8. [Class (MaskFilter)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-maskfilter)
###### 5.2.1.6.9. [Class (Matrix)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-matrix)
###### 5.2.1.6.10. [Class (Path)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-path)
###### 5.2.1.6.11. [Class (PathEffect)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-patheffect)
###### 5.2.1.6.12. [Class (PathIterator)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-pathiterator)
###### 5.2.1.6.13. [Class (Pen)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-pen)
###### 5.2.1.6.14. [Class (PointUtils)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-pointutils)
###### 5.2.1.6.15. [Class (RectUtils)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-rectutils)
###### 5.2.1.6.16. [Class (Region)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-region)
###### 5.2.1.6.17. [Class (RoundRect)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-roundrect)
###### 5.2.1.6.18. [Class (SamplingOptions)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-samplingoptions)
###### 5.2.1.6.19. [Class (ShaderEffect)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-shadereffect)
###### 5.2.1.6.20. [Class (ShadowLayer)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-shadowlayer)
###### 5.2.1.6.21. [Class (TextBlob)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-textblob)
###### 5.2.1.6.22. [Class (Tool)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-tool)
###### 5.2.1.6.23. [Class (Typeface)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-typeface)
###### 5.2.1.6.24. [Class (TypefaceArguments)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-typefacearguments)
###### 5.2.1.6.25. [Interfaces (其他)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-i)
###### 5.2.1.6.26. [Enums](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-e)
##### 5.2.1.7. [@ohos.graphics.hdrCapability (HDR能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hdrcapability)
##### 5.2.1.8. [@ohos.graphics.text (文本模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-graphics-text)
##### 5.2.1.9. [@ohos.graphics.uiEffect (效果级联)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uieffect)
#### 5.2.2. C API

##### 5.2.2.1. 模块

###### 5.2.2.1.1. [OH_NativeBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer)
###### 5.2.2.1.2. [NativeColorSpaceManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativecolorspacemanager)
###### 5.2.2.1.3. [NativeDisplaySoloist](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaysoloist)
###### 5.2.2.1.4. [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)
###### 5.2.2.1.5. [effectKit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-effectkit)
###### 5.2.2.1.6. [OH_NativeImage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativeimage)
###### 5.2.2.1.7. [NativeVsync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativevsync)
###### 5.2.2.1.8. [NativeWindow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativewindow)
###### 5.2.2.1.9. [NativeFence](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativefence)
##### 5.2.2.2. 头文件

###### 5.2.2.2.1. [buffer_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-buffer-common-h)
###### 5.2.2.2.2. [native_buffer.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-buffer-h)
###### 5.2.2.2.3. [native_color_space_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-color-space-manager-h)
###### 5.2.2.2.4. [native_display_soloist.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-display-soloist-h)
###### 5.2.2.2.5. [drawing_bitmap.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-bitmap-h)
###### 5.2.2.2.6. [drawing_brush.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-brush-h)
###### 5.2.2.2.7. [drawing_canvas.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-canvas-h)
###### 5.2.2.2.8. [drawing_color.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-color-h)
###### 5.2.2.2.9. [drawing_color_filter.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-color-filter-h)
###### 5.2.2.2.10. [drawing_color_space.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-color-space-h)
###### 5.2.2.2.11. [drawing_error_code.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-error-code-h)
###### 5.2.2.2.12. [drawing_filter.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-filter-h)
###### 5.2.2.2.13. [drawing_font.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-font-h)
###### 5.2.2.2.14. [drawing_font_collection.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-font-collection-h)
###### 5.2.2.2.15. [drawing_font_mgr.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-font-mgr-h)
###### 5.2.2.2.16. [drawing_gpu_context.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-gpu-context-h)
###### 5.2.2.2.17. [drawing_image.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-image-h)
###### 5.2.2.2.18. [drawing_image_filter.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-image-filter-h)
###### 5.2.2.2.19. [drawing_lattice.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-lattice-h)
###### 5.2.2.2.20. [drawing_mask_filter.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-mask-filter-h)
###### 5.2.2.2.21. [drawing_matrix.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-matrix-h)
###### 5.2.2.2.22. [drawing_memory_stream.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-memory-stream-h)
###### 5.2.2.2.23. [drawing_path.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-path-h)
###### 5.2.2.2.24. [drawing_path_effect.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-path-effect-h)
###### 5.2.2.2.25. [drawing_path_iterator.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-path-iterator-h)
###### 5.2.2.2.26. [drawing_pen.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-pen-h)
###### 5.2.2.2.27. [drawing_pixel_map.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-pixel-map-h)
###### 5.2.2.2.28. [drawing_point.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-point-h)
###### 5.2.2.2.29. [drawing_record_cmd.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-record-cmd-h)
###### 5.2.2.2.30. [drawing_rect.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-rect-h)
###### 5.2.2.2.31. [drawing_region.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-region-h)
###### 5.2.2.2.32. [drawing_register_font.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-register-font-h)
###### 5.2.2.2.33. [drawing_round_rect.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-round-rect-h)
###### 5.2.2.2.34. [drawing_sampling_options.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-sampling-options-h)
###### 5.2.2.2.35. [drawing_shader_effect.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-shader-effect-h)
###### 5.2.2.2.36. [drawing_shadow_layer.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-shadow-layer-h)
###### 5.2.2.2.37. [drawing_surface.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-surface-h)
###### 5.2.2.2.38. [drawing_text_blob.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-blob-h)
###### 5.2.2.2.39. [drawing_text_declaration.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-declaration-h)
###### 5.2.2.2.40. [drawing_text_font_descriptor.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-font-descriptor-h)
###### 5.2.2.2.41. [drawing_text_global.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-global-h)
###### 5.2.2.2.42. [drawing_text_line.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-line-h)
###### 5.2.2.2.43. [drawing_text_lineTypography.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-linetypography-h)
###### 5.2.2.2.44. [drawing_text_run.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-run-h)
###### 5.2.2.2.45. [drawing_text_typography.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-typography-h)
###### 5.2.2.2.46. [drawing_typeface.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-typeface-h)
###### 5.2.2.2.47. [drawing_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-types-h)
###### 5.2.2.2.48. [effect_filter.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-effect-filter-h)
###### 5.2.2.2.49. [effect_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-effect-types-h)
###### 5.2.2.2.50. [native_image.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-image-h)
###### 5.2.2.2.51. [native_vsync.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-vsync-h)
###### 5.2.2.2.52. [buffer_handle.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-buffer-handle-h)
###### 5.2.2.2.53. [external_window.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-external-window-h)
###### 5.2.2.2.54. [graphic_error_code.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-graphic-error-code-h)
###### 5.2.2.2.55. [native_fence.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-fence-h)
##### 5.2.2.3. 结构体

###### 5.2.2.3.1. [OH_NativeBuffer_ColorXY](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer-oh-nativebuffer-colorxy)
###### 5.2.2.3.2. [OH_NativeBuffer_Smpte2086](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer-oh-nativebuffer-smpte2086)
###### 5.2.2.3.3. [OH_NativeBuffer_Cta861](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer-oh-nativebuffer-cta861)
###### 5.2.2.3.4. [OH_NativeBuffer_StaticMetadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer-oh-nativebuffer-staticmetadata)
###### 5.2.2.3.5. [OH_NativeBuffer_Config](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer-oh-nativebuffer-config)
###### 5.2.2.3.6. [OH_NativeBuffer_Plane](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer-oh-nativebuffer-plane)
###### 5.2.2.3.7. [OH_NativeBuffer_Planes](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer-oh-nativebuffer-planes)
###### 5.2.2.3.8. [OH_NativeBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer-oh-nativebuffer)
###### 5.2.2.3.9. [ColorSpacePrimaries](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativecolorspacemanager-colorspaceprimaries)
###### 5.2.2.3.10. [WhitePointArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativecolorspacemanager-whitepointarray)
###### 5.2.2.3.11. [DisplaySoloist_ExpectedRateRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaysoloist-displaysoloist-expectedraterange)
###### 5.2.2.3.12. [OH_Drawing_BitmapFormat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-bitmapformat)
###### 5.2.2.3.13. [OH_Drawing_Font_Metrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-font-metrics)
###### 5.2.2.3.14. [OH_Drawing_GpuContextOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-gpucontextoptions)
###### 5.2.2.3.15. [OH_Drawing_RunBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-runbuffer)
###### 5.2.2.3.16. [OH_Drawing_PlaceholderSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-placeholderspan)
###### 5.2.2.3.17. [OH_Drawing_FontDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontdescriptor)
###### 5.2.2.3.18. [OH_Drawing_LineMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-linemetrics)
###### 5.2.2.3.19. [OH_Drawing_FontFallbackInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontfallbackinfo)
###### 5.2.2.3.20. [OH_Drawing_FontFallbackGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontfallbackgroup)
###### 5.2.2.3.21. [OH_Drawing_FontAdjustInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontadjustinfo)
###### 5.2.2.3.22. [OH_Drawing_FontAliasInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontaliasinfo)
###### 5.2.2.3.23. [OH_Drawing_FontGenericInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontgenericinfo)
###### 5.2.2.3.24. [OH_Drawing_FontConfigInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontconfiginfo)
###### 5.2.2.3.25. [OH_Drawing_FontStyleStruct](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontstylestruct)
###### 5.2.2.3.26. [OH_Drawing_FontFeature](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontfeature)
###### 5.2.2.3.27. [OH_Drawing_StrutStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-strutstyle)
###### 5.2.2.3.28. [OH_Drawing_RectSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-rectsize)
###### 5.2.2.3.29. [OH_Drawing_Point2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-point2d)
###### 5.2.2.3.30. [OH_Drawing_Point3D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-point3d)
###### 5.2.2.3.31. [OH_Drawing_Image_Info](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-image-info)
###### 5.2.2.3.32. [OH_Drawing_RectStyle_Info](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-rectstyle-info)
###### 5.2.2.3.33. [OH_Drawing_String](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-string)
###### 5.2.2.3.34. [OH_Filter_ColorMatrix](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-effectkit-oh-filter-colormatrix)
###### 5.2.2.3.35. [OH_OnFrameAvailableListener](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativeimage-oh-onframeavailablelistener)
###### 5.2.2.3.36. [OH_NativeVSync_ExpectedRateRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativevsync-oh-nativevsync-expectedraterange)
###### 5.2.2.3.37. [BufferHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativewindow-bufferhandle)
###### 5.2.2.3.38. [Region](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativewindow-region)
###### 5.2.2.3.39. [Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativewindow-rect)
###### 5.2.2.3.40. [OHHDRMetaData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativewindow-ohhdrmetadata)
###### 5.2.2.3.41. [OHExtDataHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativewindow-ohextdatahandle)
###### 5.2.2.3.42. [OH_NativeColorSpaceManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativecolorspacemanager-oh-nativecolorspacemanager)
###### 5.2.2.3.43. [OH_DisplaySoloist](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaysoloist-oh-displaysoloist)
###### 5.2.2.3.44. [NativePixelMap_](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-nativepixelmap-)
###### 5.2.2.3.45. [OH_PixelmapNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-pixelmapnative)
###### 5.2.2.3.46. [OH_Drawing_FontCollection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontcollection)
###### 5.2.2.3.47. [OH_Drawing_Typography](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-typography)
###### 5.2.2.3.48. [OH_Drawing_TextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-textstyle)
###### 5.2.2.3.49. [OH_Drawing_TypographyStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-typographystyle)
###### 5.2.2.3.50. [OH_Drawing_LineTypography](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-linetypography)
###### 5.2.2.3.51. [OH_Drawing_TypographyCreate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-typographycreate)
###### 5.2.2.3.52. [OH_Drawing_TextBox](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-textbox)
###### 5.2.2.3.53. [OH_Drawing_PositionAndAffinity](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-positionandaffinity)
###### 5.2.2.3.54. [OH_Drawing_Range](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-range)
###### 5.2.2.3.55. [OH_Drawing_TextShadow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-textshadow)
###### 5.2.2.3.56. [OH_Drawing_FontParser](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontparser)
###### 5.2.2.3.57. [OH_Drawing_TextTab](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-texttab)
###### 5.2.2.3.58. [OH_Drawing_TextLine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-textline)
###### 5.2.2.3.59. [OH_Drawing_Run](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-run)
###### 5.2.2.3.60. [OH_Drawing_FontFullDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontfulldescriptor)
###### 5.2.2.3.61. [OH_Drawing_FontVariationAxis](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontvariationaxis)
###### 5.2.2.3.62. [OH_Drawing_FontVariationInstance](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontvariationinstance)
###### 5.2.2.3.63. [OH_Drawing_FontVariationInstanceCoordinate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontvariationinstancecoordinate)
###### 5.2.2.3.64. [OH_Drawing_Canvas](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-canvas)
###### 5.2.2.3.65. [OH_Drawing_Pen](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-pen)
###### 5.2.2.3.66. [OH_Drawing_Region](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-region)
###### 5.2.2.3.67. [OH_Drawing_Brush](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-brush)
###### 5.2.2.3.68. [OH_Drawing_Path](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-path)
###### 5.2.2.3.69. [OH_Drawing_PathIterator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-pathiterator)
###### 5.2.2.3.70. [OH_Drawing_Lattice](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-lattice)
###### 5.2.2.3.71. [OH_Drawing_Bitmap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-bitmap)
###### 5.2.2.3.72. [OH_Drawing_Point](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-point)
###### 5.2.2.3.73. [OH_Drawing_PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-pixelmap)
###### 5.2.2.3.74. [OH_Drawing_ColorSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-colorspace)
###### 5.2.2.3.75. [OH_Drawing_PathEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-patheffect)
###### 5.2.2.3.76. [OH_Drawing_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-rect)
###### 5.2.2.3.77. [OH_Drawing_RoundRect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-roundrect)
###### 5.2.2.3.78. [OH_Drawing_Matrix](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-matrix)
###### 5.2.2.3.79. [OH_Drawing_ShaderEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-shadereffect)
###### 5.2.2.3.80. [OH_Drawing_ShadowLayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-shadowlayer)
###### 5.2.2.3.81. [OH_Drawing_Filter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-filter)
###### 5.2.2.3.82. [OH_Drawing_MaskFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-maskfilter)
###### 5.2.2.3.83. [OH_Drawing_ColorFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-colorfilter)
###### 5.2.2.3.84. [OH_Drawing_Font](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-font)
###### 5.2.2.3.85. [OH_Drawing_FontFeatures](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontfeatures)
###### 5.2.2.3.86. [OH_Drawing_MemoryStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-memorystream)
###### 5.2.2.3.87. [OH_Drawing_FontArguments](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontarguments)
###### 5.2.2.3.88. [OH_Drawing_Typeface](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-typeface)
###### 5.2.2.3.89. [OH_Drawing_TextBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-textblob)
###### 5.2.2.3.90. [OH_Drawing_Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-image)
###### 5.2.2.3.91. [OH_Drawing_ImageFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-imagefilter)
###### 5.2.2.3.92. [OH_Drawing_SamplingOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-samplingoptions)
###### 5.2.2.3.93. [OH_Drawing_TextBlobBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-textblobbuilder)
###### 5.2.2.3.94. [OH_Drawing_GpuContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-gpucontext)
###### 5.2.2.3.95. [OH_Drawing_Surface](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-surface)
###### 5.2.2.3.96. [OH_Drawing_FontMgr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontmgr)
###### 5.2.2.3.97. [OH_Drawing_FontStyleSet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontstyleset)
###### 5.2.2.3.98. [OH_Drawing_RecordCmdUtils](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-recordcmdutils)
###### 5.2.2.3.99. [OH_Drawing_RecordCmd](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-recordcmd)
###### 5.2.2.3.100. [OH_Drawing_Array](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-array)
###### 5.2.2.3.101. [OH_Filter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-effectkit-oh-filter)
###### 5.2.2.3.102. [OH_NativeImage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativeimage-oh-nativeimage)
###### 5.2.2.3.103. [NativeWindow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativewindow-nativewindow)
###### 5.2.2.3.104. [NativeWindowBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativewindow-nativewindowbuffer)
###### 5.2.2.3.105. [OH_NativeVSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativevsync-oh-nativevsync)
###### 5.2.2.3.106. [OHIPCParcel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativewindow-ohipcparcel)
#### 5.2.3. 错误码

##### 5.2.3.1. [色彩管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-colorspace-manager)
##### 5.2.3.2. [图形绘制与显示错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-drawing)
### 5.3. ArkGraphics 3D（方舟3D图形）

#### 5.3.1. ArkTS API

##### 5.3.1.1. [@ohos.graphics.scene (ArkGraphics 3D模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-scene)
##### 5.3.1.2. graphics3d

###### 5.3.1.2.1. [Scene](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene)
###### 5.3.1.2.2. [SceneNode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-nodes)
###### 5.3.1.2.3. [SceneType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-types)
###### 5.3.1.2.4. [SceneResource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-resources)
###### 5.3.1.2.5. [ScenePostProcessSettings](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-post-process-settings)
### 5.4. Graphics Accelerate Kit（图形加速服务）

#### 5.4.1. ArkTS API

##### 5.4.1.1. [assetDownloadManager（资源包下载管理）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/graphics-accelerate-assetdownloadmanager)
##### 5.4.1.2. [AssetAccelerationExtensionAbility（资源加速ExtensionAbility）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/graphics-accelerate-extensionability)
##### 5.4.1.3. [AssetAccelerationExtensionContext（资源加速ExtensionContext）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/graphics-accelerate-extensioncontext)
##### 5.4.1.4. [launchAcceleration（游戏启动加速）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/graphics-accelerate-launchacceleration)
##### 5.4.1.5. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-graphics-accelerate)
#### 5.4.2. C API

##### 5.4.2.1. 模块

###### 5.4.2.1.1. [GraphicsAccelerate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate)
##### 5.4.2.2. 头文件和结构体

###### 5.4.2.2.1. 头文件

###### 5.4.2.2.1.1. [abr_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/abr__base_8h)
###### 5.4.2.2.1.2. [abr_gles.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/abr__gles_8h)
###### 5.4.2.2.1.3. [frame_generation_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/frame__generation__base_8h)
###### 5.4.2.2.1.4. [frame_generation_gles.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/frame__generation__gles_8h)
###### 5.4.2.2.1.5. [frame_generation_vk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/frame__generation__vk_8h)
###### 5.4.2.2.1.6. [opengtx_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/opengtx__base_8h)
###### 5.4.2.2.2. 结构体

###### 5.4.2.2.2.1. [ABR_CameraData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_a_b_r___camera_data)
###### 5.4.2.2.2.2. [ABR_Vector3](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_a_b_r___vector3)
###### 5.4.2.2.2.3. [FG_AlgorithmModeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___algorithm_mode_info)
###### 5.4.2.2.2.4. [FG_ContextDescription_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___context_description___v_k)
###### 5.4.2.2.2.5. [FG_Dimension2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___dimension2_d)
###### 5.4.2.2.2.6. [FG_DispatchDescription_GLES](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___dispatch_description___g_l_e_s)
###### 5.4.2.2.2.7. [FG_DispatchDescription_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___dispatch_description___v_k)
###### 5.4.2.2.2.8. [FG_ImageFormat_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___image_format___v_k)
###### 5.4.2.2.2.9. [FG_ImageInfo_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___image_info___v_k)
###### 5.4.2.2.2.10. [FG_ImageSync_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___image_sync___v_k)
###### 5.4.2.2.2.11. [FG_Mat4x4](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___mat4x4)
###### 5.4.2.2.2.12. [FG_ResolutionInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___resolution_info)
###### 5.4.2.2.2.13. [FG_Vec3D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___vec3_d)
###### 5.4.2.2.2.14. [FG_PerFrameExtendedCameraInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___per_frame_extended_camera_info)
###### 5.4.2.2.2.15. [FG_IntegrationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___intergration_info)
###### 5.4.2.2.2.16. [OpenGTX_ConfigDescription](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___config_description)
###### 5.4.2.2.2.17. [OpenGTX_FrameRenderInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___frame_render_info)
###### 5.4.2.2.2.18. [OpenGTX_GameSceneInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___game_scene_info)
###### 5.4.2.2.2.19. [OpenGTX_NetworkInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___network_info)
###### 5.4.2.2.2.20. [OpenGTX_NetworkLatency](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___network_latency)
###### 5.4.2.2.2.21. [OpenGTX_ResolutionValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___resolution_value)
###### 5.4.2.2.2.22. [OpenGTX_Vector3](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___vector3)
### 5.5. Spatial Recon Kit（空间建模服务）

#### 5.5.1. ArkTS API

##### 5.5.1.1. [spatialRender](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/spatial-recon-spatialrender)
##### 5.5.1.2. [spatialEdit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/spatial-recon-spatialedit)
##### 5.5.1.3. [spatialImage（空间照片）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/spatial-recon-spatialimage)
#### 5.5.2. C API

##### 5.5.2.1. 模块

###### 5.5.2.1.1. [SpatialRecon](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-spatialrecon)
##### 5.5.2.2. 头文件和结构体

###### 5.5.2.2.1. 头文件

###### 5.5.2.2.1.1. [spatial_recon_interface.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-spatial-recon-interface-h)
###### 5.5.2.2.2. 结构体

###### 5.5.2.2.2.1. [HMS_SpatialRecon_ModelWriteInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-spatialrecon-hms-spatialrecon-modelwriteinfo)
###### 5.5.2.2.2.2. [HMS_SpatialRecon_DataFrame](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-spatialrecon-hms-spatialrecon-dataframe)
###### 5.5.2.2.2.3. [HMS_SpatialRecon_Session](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-spatialrecon-hms-spatialrecon-session)
###### 5.5.2.2.2.4. [AREngine_ARSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-spatialrecon-arengine-arsession)
###### 5.5.2.2.2.5. [AREngine_ARFrame](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-spatialrecon-arengine-arframe)
### 5.6. XEngine Kit（GPU加速引擎服务）

#### 5.6.1. C API

##### 5.6.1.1. 模块

###### 5.6.1.1.1. [XEngine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine)
##### 5.6.1.2. 头文件和结构体

###### 5.6.1.2.1. 头文件

###### 5.6.1.2.1.1. [xeg_extension_defs.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-extension-defs-8h)
###### 5.6.1.2.1.2. [xeg_gles_adaptive_vrs.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-gles-adaptive-vrs-8h)
###### 5.6.1.2.1.3. [xeg_gles_extension.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-gles-extension-8h)
###### 5.6.1.2.1.4. [xeg_gles_neural_upscale.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-gles-neural-upscale-8h)
###### 5.6.1.2.1.5. [xeg_gles_spatial_upscale.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-gles-spatial-upscale-8h)
###### 5.6.1.2.1.6. [xeg_gles_temporal_upscale.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-gles-temporal-upscale-8h)
###### 5.6.1.2.1.7. [xeg_vulkan_adaptive_vrs.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-adaptive-vrs-8h)
###### 5.6.1.2.1.8. [xeg_vulkan_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-common-8h)
###### 5.6.1.2.1.9. [xeg_vulkan_extension.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-extension-8h)
###### 5.6.1.2.1.10. [xeg_vulkan_hps.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-hps-8h)
###### 5.6.1.2.1.11. [xeg_vulkan_rt_reflection.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-rt-reflection-8h)
###### 5.6.1.2.1.12. [xeg_vulkan_rt_visible_mask.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-rt-visible-mask-8h)
###### 5.6.1.2.1.13. [xeg_vulkan_rtgi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-rtgi-8h)
###### 5.6.1.2.1.14. [xeg_vulkan_spatial_upscale.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-spatial-upscale-8h)
###### 5.6.1.2.1.15. [xeg_vulkan_temporal_upscale.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-temporal-upscale-8h)
###### 5.6.1.2.1.16. [xeg_vulkan_neural_upscale.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-neural-upscale-8h)
###### 5.6.1.2.1.17. [xeg_control_display_separation.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-control-display-separation)
###### 5.6.1.2.2. 结构体

###### 5.6.1.2.2.1. [XEG_AdaptiveVRSCreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-adaptivevrscreateinfo)
###### 5.6.1.2.2.2. [XEG_AdaptiveVRSDescription](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-adaptivevrsdescription)
###### 5.6.1.2.2.3. [XEG_DDGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgicreateinfo)
###### 5.6.1.2.2.4. [XEG_DDGIDescription](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgidescription)
###### 5.6.1.2.2.5. [XEG_DDGIVolumeEntryParameters](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgivolumeentryparameters)
###### 5.6.1.2.2.6. [XEG_ExtensionProperties](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-extensionproperties)
###### 5.6.1.2.2.7. [XEG_HPSCreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-hpscreateinfo)
###### 5.6.1.2.2.8. [XEG_HPSRadixSort](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-hpsradixsort)
###### 5.6.1.2.2.9. [XEG_HPSRadixSortDescription](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-hpsradixsortdescription)
###### 5.6.1.2.2.10. [XEG_NNGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngicreateinfo)
###### 5.6.1.2.2.11. [XEG_NNGIDescription](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngidescription)
###### 5.6.1.2.2.12. [XEG_RTAOParameters](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-rtaoparameters)
###### 5.6.1.2.2.13. [XEG_RTReflectionCreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-rtreflectioncreateinfo)
###### 5.6.1.2.2.14. [XEG_RTReflectionDescription](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-rtreflectiondescription)
###### 5.6.1.2.2.15. [XEG_RTShadowAOCreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-rtshadowaocreateinfo)
###### 5.6.1.2.2.16. [XEG_RTShadowAODenoiserParameters](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-rtshadowaodenoiserparameters)
###### 5.6.1.2.2.17. [XEG_RTShadowAODescription](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-rtshadowaodescription)
###### 5.6.1.2.2.18. [XEG_RTShadowParameters](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-rtshadowparameters)
###### 5.6.1.2.2.19. [XEG_SpatialUpscaleCreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-spatialupscalecreateinfo)
###### 5.6.1.2.2.20. [XEG_SpatialUpscaleDescription](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-spatialupscaledescription)
###### 5.6.1.2.2.21. [XEG_TemporalUpscaleCreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-temporalupscalecreateinfo)
###### 5.6.1.2.2.22. [XEG_TemporalUpscaleDescription](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-temporalupscaledescription)
###### 5.6.1.2.2.23. [XEG_NeuralUpscaleCreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-neuralupscalecreateinfo)
###### 5.6.1.2.2.24. [XEG_NeuralUpscaleDescription](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-neuralupscaledescription)

## 6. 应用服务

### 6.1. Account Kit（华为账号服务）

#### 6.1.1. ArkTS API

##### 6.1.1.1. [@hms.core.authentication (华为账号应用统一认证服务)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-authentication)
##### 6.1.1.2. [@hms.core.account.extendService (华为账号增强服务)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-extendservice)
##### 6.1.1.3. [@hms.core.account.shippingAddress (华为账号收货地址管理服务)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-choose-address)
##### 6.1.1.4. [@hms.core.account.minorsProtection (华为账号未成年人模式)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-minorsprotection)
##### 6.1.1.5. [@hms.core.account.invoiceAssistant (华为账号发票助手服务)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-invoiceassistant)
##### 6.1.1.6. [@hms.core.account.realName (华为账号实名认证服务)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-realname)
#### 6.1.2. ArkTS组件

##### 6.1.2.1. [LoginPanel (华为账号Panel登录组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-loginpanel)
##### 6.1.2.2. [LoginWithHuaweiIDButton (华为账号Button登录组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-huawei-id-button)
##### 6.1.2.3. [loginComponentManager (华为账号登录组件管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-component-manager)
#### 6.1.3. [ArkTS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account-kit)
#### 6.1.4. REST API

##### 6.1.4.1. [公共说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-common)
##### 6.1.4.2. 开放接口调用凭证

###### 6.1.4.2.1. [概述](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-obtain-token-overview)
###### 6.1.4.2.2. [获取用户级凭证](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-obtain-user-token)
###### 6.1.4.2.3. [刷新用户级凭证](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-obtain-refresh-token)
###### 6.1.4.2.4. [解析凭证](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-get-token-info)
###### 6.1.4.2.5. [取消用户级凭证授权](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-obtain-revoke-token)
###### 6.1.4.2.6. [获取应用级凭证](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-obtain-app-token)
##### 6.1.4.3. 获取用户信息

###### 6.1.4.3.1. [概述](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-get-user-info-overview)
###### 6.1.4.3.2. [一键登录获取华为账号绑定号码和UnionID/OpenID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-get-user-info-quicklogin-by-code)
###### 6.1.4.3.3. [获取华为账号用户信息-获取头像昵称](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-get-user-info-get-nickname-and-avatar)
###### 6.1.4.3.4. [获取华为账号用户信息-获取手机号](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-get-user-info-get-phone)
###### 6.1.4.3.5. [获取用户风险等级](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-getuserrisklevel)
##### 6.1.4.4. 实名认证

###### 6.1.4.4.1. [概述](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-realname-overview)
###### 6.1.4.4.2. [获取实名信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-get-realname)
###### 6.1.4.4.3. [获取用户实名年龄段](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-get-realname-age-range-flag)
###### 6.1.4.4.4. [实名信息校验](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-verify-realname)
##### 6.1.4.5. 扩展能力

###### 6.1.4.5.1. [通过OpenID获取UnionID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-get-unionid)
###### 6.1.4.5.2. [通过Authorization Code获取GroupUnionID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-get-groupunionid-code)
###### 6.1.4.5.3. [通过OpenID或UnionID获取GroupUnionID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-get-groupunionid)
###### 6.1.4.5.4. [获取验证ID Token的JWT公钥信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-rest-jwt-public-key)
###### 6.1.4.5.5. [验证ID Token有效性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-verify-id-token)
###### 6.1.4.5.6. [获取OpenID Connect配置公开信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-rest-openid-configuration)
##### 6.1.4.6. 附录

###### 6.1.4.6.1. [一键登录获取华为账号绑定号码和UnionID/OpenID（不推荐）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-get-user-info-quicklogin-getid)
##### 6.1.4.7. [REST API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-server-error-code)
### 6.2. Ads Kit（广告服务）

#### 6.2.1. ArkTS API

##### 6.2.1.1. [@ohos.advertising (广告服务框架)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-advertising)
##### 6.2.1.2. [@ohos.identifier.oaid (开放匿名设备标识服务)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-oaid)
##### 6.2.1.3. [@ohos.advertising.AdsServiceExtensionAbility(广告扩展服务)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-adsserviceextensionability)
##### 6.2.1.4. advertisement

###### 6.2.1.4.1. [advertisement (广告内容)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-advertisement)
#### 6.2.2. ArkTS组件

##### 6.2.2.1. [@ohos.advertising.AdComponent (广告展示组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-adcomponent)
##### 6.2.2.2. [@ohos.advertising.AutoAdComponent (轮播广告展示组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-autoadcomponent)
#### 6.2.3. 错误码

##### 6.2.3.1. [广告服务框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-ads)
##### 6.2.3.2. [开放匿名设备标识服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-oaid)
### 6.3. AppGallery Kit（应用市场服务）

#### 6.3.1. ArkTS API

##### 6.3.1.1. [moduleInstallManager (产品特性按需分发)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-moduleinstallmanager)
##### 6.3.1.2. [productViewManager (应用市场推荐)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-productviewmanager)
##### 6.3.1.3. [sceneManager （生态查询服务）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-scenemanager)
##### 6.3.1.4. [updateManager（更新功能）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-updatemanager)
##### 6.3.1.5. [attributionManager（应用归因服务）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-attributionmanager)
##### 6.3.1.6. [attributionTestManager（应用归因接入调试功能）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-attributiontestmanager)
##### 6.3.1.7. [privacyManager（隐私管理服务）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-privacymanager)
##### 6.3.1.8. [appInfoManager（应用元数据管理服务）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/appgallery-appinfomanager)
##### 6.3.1.9. [commentManager（应用评论服务）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/appgallery-commentmanager)
##### 6.3.1.10. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-appgallery)
#### 6.3.2. C API

##### 6.3.2.1. 模块

###### 6.3.2.1.1. [ModuleInstall](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-c-moduleinstall)
##### 6.3.2.2. 头文件

###### 6.3.2.2.1. [module_install.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-c-module_install)
#### 6.3.3. REST API

##### 6.3.3.1. [归因结果回传](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-rest-receive)
### 6.4. App Linking Kit（应用链接服务）

#### 6.4.1. ArkTS API

##### 6.4.1.1. [deferredLink (延迟链接能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/applinking-deferredlink-api)
### 6.5. Calendar Kit（日历服务）

#### 6.5.1. ArkTS API

##### 6.5.1.1. [@ohos.calendarManager (日程管理能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-calendarmanager)
#### 6.5.2. 错误码

##### 6.5.2.1. [日历服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-calendarmanager)
### 6.6. Call Service Kit（通话服务）

#### 6.6.1. ArkTS API

##### 6.6.1.1. [voipCall (应用内通话管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/call-voipcall)
##### 6.6.1.2. [CallerInfoQueryExtensionAbility (来去电信息查询扩展Ability)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/callservicekit-callerinfoquery-extension-ability)
##### 6.6.1.3. [CallerInfoQueryExtensionContext (来去电信息查询扩展Context)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/callservicekit-callerinfoquery-extension-context)
##### 6.6.1.4. [numberIdentify (号码识别查询基本能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/callservicekit-numberldentify)
##### 6.6.1.5. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/call-error-code)
### 6.7. Cloud Foundation Kit（云开发服务）

#### 6.7.1. ArkTS API

##### 6.7.1.1. [cloudCommon (公共模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cloudfoundation-cloudcommon)
##### 6.7.1.2. [cloudFunction (云函数模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cloudfoundation-cloudfunction)
##### 6.7.1.3. [cloudStorage (云存储模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cloudfoundation-cloudstorage)
##### 6.7.1.4. [cloudDatabase (云数据库模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cloudfoundation-clouddatabase)
##### 6.7.1.5. [cloudResPrefetch（预加载模块）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cloudfoundation-cloudresprefetch)
##### 6.7.1.6. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-cloudfoundation)
### 6.8. Contacts Kit（联系人服务）

#### 6.8.1. ArkTS API

##### 6.8.1.1. [@ohos.contact (联系人)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-contact)
#### 6.8.2. 错误码

##### 6.8.2.1. [Contacts错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-contacts)
### 6.9. Enterprise Space Kit（企业数字空间服务）

#### 6.9.1. ArkTS API

##### 6.9.1.1. [@hms.enterpriseSpaceService.fileTransfer(空间数据传输)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/enterprisespace-spacedatatransfer)
##### 6.9.1.2. [@hms.enterpriseSpaceService.spaceManager(空间管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/enterprisespace-spacemanager)
##### 6.9.1.3. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-enterprise-space)
### 6.10. File Manager Service Kit（文件管理服务）

#### 6.10.1. ArkTS API

##### 6.10.1.1. [fileManagerService](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/filemanagerservice-arkts-filemanagerservice)
##### 6.10.1.2. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/filemanagerservice-arkts-errorcode)
#### 6.10.2. [图标格式说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/filemanagerservice-iconformat)
### 6.11. Game Controller Kit（游戏控制器服务）

#### 6.11.1. C API

##### 6.11.1.1. 模块

###### 6.11.1.1.1. [GameController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-controller)
##### 6.11.1.2. 头文件和结构体

###### 6.11.1.2.1. 头文件

###### 6.11.1.2.1.1. [game_controller_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-controller-type)
###### 6.11.1.2.1.2. [game_device.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-device)
###### 6.11.1.2.1.3. [game_device_event.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-device-event)
###### 6.11.1.2.1.4. [game_pad.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-pad)
###### 6.11.1.2.1.5. [game_pad_event.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-pad-event)
#### 6.11.2. [错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gamecontroller-c-error-code)
### 6.12. Game Service Kit（游戏服务）

#### 6.12.1. ArkTS API

##### 6.12.1.1. [gamePlayer（基础游戏服务）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gameservice-gameplayer)
##### 6.12.1.2. [gamePerformance（游戏场景感知）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gameservice-gameperformance)
##### 6.12.1.3. [gameNearbyTransfer（游戏近场快传）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gameservice-nearbytransfer)
##### 6.12.1.4. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-gameservice)
#### 6.12.2. C API

##### 6.12.2.1. 模块

###### 6.12.2.1.1. [GamePerformance](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gameservice-game-performance)
##### 6.12.2.2. 头文件和结构体

###### 6.12.2.2.1. 头文件

###### 6.12.2.2.1.1. [game_performance.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gameservice-game-performance-h)
##### 6.12.2.3. [C API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gameservice-c-error-code)
#### 6.12.3. REST API

##### 6.12.3.1. [获取玩家标识](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gameservice-getplayerinfo)
##### 6.12.3.2. [转换ID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gameservice-convertid)
##### 6.12.3.3. [批量转换teamPlayerId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gameservice-teamplayerid)
##### 6.12.3.4. [解绑账号](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gameservice-unbindplayer)
##### 6.12.3.5. [解绑账号通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gameservice-unbindplayer-notification)
### 6.13. Health Service Kit（运动健康服务）

#### 6.13.1. ArkTS API

##### 6.13.1.1. [healthStore (运动健康数据服务)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore)
##### 6.13.1.2. [healthService (运动健康联动服务)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthservice)
##### 6.13.1.3. [healthStore (运动健康数据服务)(Lite)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore-lite)
##### 6.13.1.4. [healthService (运动健康联动服务)(Lite)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthservice-lite)
##### 6.13.1.5. 运动健康数据类型常量及模型定义

###### 6.13.1.5.1. [healthDataTypes (运动健康数据类型常量)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthdatatypes)
###### 6.13.1.5.2. [healthFields (运动健康数据字段)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthfields)
###### 6.13.1.5.3. [healthModels (运动健康数据模型)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthmodels)
###### 6.13.1.5.4. [samplePointHelper (采样数据类型常量)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-samplepointhelper)
###### 6.13.1.5.5. [healthSequenceHelper (健康记录类型常量)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthsequencehelper)
###### 6.13.1.5.6. [exerciseSequenceHelper (锻炼记录类型常量)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-exercisedequencehelper)
###### 6.13.1.5.7. [healthDataTypes (运动健康数据类型常量)(Lite)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthdatatypes-lite)
###### 6.13.1.5.8. [healthFields (运动健康数据字段)(Lite)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthfields-lite)
###### 6.13.1.5.9. [exerciseSequenceHelper (锻炼记录类型常量)(Lite)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-exercisedequencehelper-lite)
###### 6.13.1.5.10. [exerciseRealtimeHelper (实时运动数据类型常量)(Lite)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-exerciserealtimehelper-lite)
#### 6.13.2. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice)
### 6.14. IAP Kit（应用内支付服务）

#### 6.14.1. ArkTS API

##### 6.14.1.1. [IAP](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-iap)
##### 6.14.1.2. [数据类型说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-data-model)
##### 6.14.1.3. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-iap)
#### 6.14.2. ArkTS组件

##### 6.14.2.1. [CashierComponent (iap嵌入式收银台组件)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-cashier-component)
##### 6.14.2.2. [cashierComponentManager (iap嵌入式收银台组件管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-cashier-component-manager)
#### 6.14.3. REST API

##### 6.14.3.1. [公共说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-rest-common-statement)
##### 6.14.3.2. [生成服务端请求的token](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-jwt-description)
##### 6.14.3.3. [对返回结果验签](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-verifying-signature)
##### 6.14.3.4. [订单状态查询（消耗型/非消耗型/非续期订阅商品）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-query-order-status)
##### 6.14.3.5. [订单确认发货（消耗型/非消耗型/非续期订阅商品）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-confirm-purchase-for-order)
##### 6.14.3.6. [应用购买记录相关支付订单查询](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-order-query)
##### 6.14.3.7. [订阅状态查询](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-query-subscription-status)
##### 6.14.3.8. [订阅确认发货](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-confirm-purchase-for-sub)
##### 6.14.3.9. [延迟订阅续订日期](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-date-delay-for-sub)
##### 6.14.3.10. [根据交易号查询订单状态信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-order-info-query-by-transaction-number)
##### 6.14.3.11. [查询用户的历史购买记录](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-order-info-query-by-order-history)
##### 6.14.3.12. [服务端通知记录查询](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-server-notifications-record-query)
##### 6.14.3.13. [测试服务端通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-server-notifications-test)
##### 6.14.3.14. [生成优惠签名购买参数](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-server-subscribe-offer-sign)
##### 6.14.3.15. [服务端关键事件通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-key-event-notifications)
##### 6.14.3.16. 退款申请通知与处理

###### 6.14.3.16.1. [接收退款申请事件通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-server-refund-receive-notify)
###### 6.14.3.16.2. [返回退款审核结果](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-server-refund-return-result)
##### 6.14.3.17. [数据类型说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-server-data-model)
##### 6.14.3.18. [REST API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/iap-server-error-code)
### 6.15. Live View Kit（实况窗服务）

#### 6.15.1. ArkTS API

##### 6.15.1.1. [liveViewManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/liveview-liveviewmanager)
##### 6.15.1.2. [LiveViewLockScreenExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/liveview-lock-screen-ability)
##### 6.15.1.3. [LiveViewLockScreenExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/liveview-lock-screen-context)
##### 6.15.1.4. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/liveview-error-code)
##### 6.15.1.5. [实况窗Live View Kit与Push Kit的API字段关联](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/liveview-api-map)
### 6.16. Location Kit（位置服务）

#### 6.16.1. ArkTS API

##### 6.16.1.1. [@ohos.geoLocationManager (位置服务)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager)
##### 6.16.1.2. [@ohos.app.ability.FenceExtensionAbility (FenceExtensionAbility)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-fenceextensionability)
##### 6.16.1.3. [@ohos.app.ability.FenceExtensionContext (FenceExtensionContext)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-fenceextensioncontext)
##### 6.16.1.4. 已停止维护的接口

###### 6.16.1.4.1. [@ohos.geolocation (位置服务)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocation)
###### 6.16.1.4.2. [@system.geolocation (地理位置)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-location)
#### 6.16.2. C API

##### 6.16.2.1. 模块

###### 6.16.2.1.1. [Location](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-location)
##### 6.16.2.2. 头文件

###### 6.16.2.2.1. [oh_location.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-location-h)
###### 6.16.2.2.2. [oh_location_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-location-type-h)
##### 6.16.2.3. 结构体

###### 6.16.2.3.1. [Location_BasicInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-location-location-basicinfo)
###### 6.16.2.3.2. [Location_RequestConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-location-location-requestconfig)
###### 6.16.2.3.3. [Location_Info](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-location-location-info)
#### 6.16.3. 错误码

##### 6.16.3.1. [位置服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-geolocationmanager)
### 6.17. Map Kit（地图服务）

#### 6.17.1. ArkTS API

##### 6.17.1.1. map（地图显示功能）

###### 6.17.1.1.1. [模块描述](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-module-desc)
###### 6.17.1.1.2. [Class (MapComponentController)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapcomponentcontroller)
###### 6.17.1.1.3. [Interface (BaseOverlay)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-baseoverlay)
###### 6.17.1.1.4. [Interface (Marker)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-marker)
###### 6.17.1.1.5. [Interface (MapPolyline)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mappolyline)
###### 6.17.1.1.6. [Interface (MapPolygon)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mappolygon)
###### 6.17.1.1.7. [Interface (MapCircle)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapcircle)
###### 6.17.1.1.8. [Interface (BasePriorityOverlay)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-basepriorityoverlay)
###### 6.17.1.1.9. [Interface (PointAnnotation)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-pointannotation)
###### 6.17.1.1.10. [Interface (Bubble)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-bubble)
###### 6.17.1.1.11. [Interface (CameraUpdate)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-cameraupdate)
###### 6.17.1.1.12. [Interface (Projection)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-projection)
###### 6.17.1.1.13. [Class (LatLngBoundsUtils)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-latlngboundsutils)
###### 6.17.1.1.14. [Class (Animation)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-animation)
###### 6.17.1.1.15. [Class (AlphaAnimation)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-alphaanimation)
###### 6.17.1.1.16. [Class (RotateAnimation)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-rotateanimation)
###### 6.17.1.1.17. [Class (ScaleAnimation)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-scaleanimation)
###### 6.17.1.1.18. [Class (TranslateAnimation)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-translateanimation)
###### 6.17.1.1.19. [Class (FontSizeAnimation)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-fontsizeanimation)
###### 6.17.1.1.20. [Class (PlayImageAnimation)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-playimageanimation)
###### 6.17.1.1.21. [Class (AnimationSet)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-animationset)
###### 6.17.1.1.22. [Interface (ClusterOverlay)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-clusteroverlay)
###### 6.17.1.1.23. [Interface (ImageOverlay)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-imageoverlay)
###### 6.17.1.1.24. [Interface (BuildingOverlay)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-buildingoverlay)
###### 6.17.1.1.25. [Interface (TraceOverlay)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-traceoverlay)
###### 6.17.1.1.26. [Interface (MapArc)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-maparc)
###### 6.17.1.1.27. [class (SpatialRelationUtil)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-spatialrelationutil)
###### 6.17.1.1.28. [Interface (AnimateResult)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-animateresult)
###### 6.17.1.1.29. [Interface (MarkerDelegate)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-markerdelegate)
###### 6.17.1.1.30. [Interface (MapEventManager)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapeventmanager)
###### 6.17.1.1.31. [Interface (MarkerClusterInfo)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-markerclusterinfo)
###### 6.17.1.1.32. [Interface (TileOverlay)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-tileoverlay)
###### 6.17.1.1.33. [Interface (IndoorMapInfo)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-indoormapinfo)
###### 6.17.1.1.34. [Interface (Heatmap)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-heatmap)
###### 6.17.1.1.35. [Interface (MvtOverlay)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mvtoverlay)
###### 6.17.1.1.36. [Interface (FlowFieldOverlay)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-flowfieldoverlay)
###### 6.17.1.1.37. [Interface (MassPointOverlay)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-masspointoverlay)
###### 6.17.1.1.38. [Types](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-types)
###### 6.17.1.1.39. [Enums](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-enums)
###### 6.17.1.1.40. [Functions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-functions)
##### 6.17.1.2. [mapCommon（地图属性模型）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common)
##### 6.17.1.3. [navi（路径规划）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-navi-api)
##### 6.17.1.4. [petalMaps（拉起地图应用）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-petal-maps)
##### 6.17.1.5. [sceneMap（场景化控件）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-scenemap)
##### 6.17.1.6. [site（地点搜索）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-site)
##### 6.17.1.7. [staticMap（静态图）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-staticmap)
##### 6.17.1.8. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-map)
##### 6.17.1.9. 附录

###### 6.17.1.9.1. [POI类型值](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-poi)
###### 6.17.1.9.2. [城市码及区划代码表](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-citycode)
###### 6.17.1.9.3. [路径规划支持的国家/地区](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-navisupported)
#### 6.17.2. ArkTS组件

##### 6.17.2.1. [MapComponent（地图组件）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-mapcomponent)
### 6.18. Notification Kit（用户通知服务）

#### 6.18.1. ArkTS API

##### 6.18.1.1. [@ohos.notificationManager (NotificationManager模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationmanager)
##### 6.18.1.2. [@ohos.notificationExtensionSubscription (notificationExtensionSubscription模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationextensionsubscription)
##### 6.18.1.3. [@ohos.application.NotificationSubscriberExtensionAbility (通知订阅扩展能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationsubscriberextensionability)
##### 6.18.1.4. [@ohos.application.NotificationSubscriberExtensionContext (通知订阅扩展上下文)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationsubscriberextensioncontext)
##### 6.18.1.5. notification

###### 6.18.1.5.1. [NotificationActionButton](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationactionbutton)
###### 6.18.1.5.2. [NotificationCommonDef](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationcommondef)
###### 6.18.1.5.3. [NotificationContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationcontent)
###### 6.18.1.5.4. [NotificationExtensionContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationextensioncontent)
###### 6.18.1.5.5. [NotificationFlags](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationflags)
###### 6.18.1.5.6. [NotificationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationinfo)
###### 6.18.1.5.7. [NotificationRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationrequest)
###### 6.18.1.5.8. [NotificationSlot](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationslot)
###### 6.18.1.5.9. [NotificationTemplate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationtemplate)
###### 6.18.1.5.10. [NotificationUserInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationuserinput)
###### 6.18.1.5.11. [NotificationExtensionSubscriptionInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notificationextensionsubscriptioninfo)
##### 6.18.1.6. 已停止维护的接口

###### 6.18.1.6.1. [@ohos.notification (Notification模块)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notification)
###### 6.18.1.6.2. [@system.notification (通知消息)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-notification)
#### 6.18.2. C API

##### 6.18.2.1. 模块

###### 6.18.2.1.1. [NOTIFICATION](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-notification)
##### 6.18.2.2. 头文件

###### 6.18.2.2.1. [notification.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-notification-h)
#### 6.18.3. 错误码

##### 6.18.3.1. [通知错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-notification)
### 6.19. Payment Kit（鸿蒙支付服务）

#### 6.19.1. ArkTS API

##### 6.19.1.1. [paymentService (鸿蒙支付服务)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-paymentservice)
##### 6.19.1.2. [realNameService(身份验证服务)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-realnameservice)
##### 6.19.1.3. [ecnyPaymentService (数字人民币服务)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-ecnypaymentservice)
##### 6.19.1.4. [thirdPaymentService(三方支付服务)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-third-payment-service)
##### 6.19.1.5. [promotionService(营销服务)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-promotionservice)
##### 6.19.1.6. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-payment)
#### 6.19.2. REST API

##### 6.19.2.1. [公共说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-rest-overview)
##### 6.19.2.2. 直连商户

###### 6.19.2.2.1. 基础支付

###### 6.19.2.2.1.1. [预下单](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-prepay)
###### 6.19.2.2.1.2. [关闭订单](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-orders-close)
###### 6.19.2.2.1.3. [支付结果回调通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-pay-notify)
####### 6.19.2.2.1.4. 查询支付订单

###### 6.19.2.2.1.4.1. [通过sysTransOrderNo查询订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-sys-query-order)
###### 6.19.2.2.1.4.2. [通过mercOrderNo查询订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-merc-query-order)
###### 6.19.2.2.1.5. [申请退款](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-service--refund)
###### 6.19.2.2.1.6. [退款结果回调通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-refund-notify)
####### 6.19.2.2.1.7. 查询退款订单

###### 6.19.2.2.1.7.1. [通过sysRefundOrderNo查询退款订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-sys-query-refund)
###### 6.19.2.2.1.7.2. [通过mercRefundOrderNo查询退款订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-merc-query-refund)
###### 6.19.2.2.2. 支付并签约

###### 6.19.2.2.2.1. [预下单](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-pas-prepay)
###### 6.19.2.2.2.2. [支付结果回调通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-pas-pay-notify)
####### 6.19.2.2.2.3. 查询支付订单

###### 6.19.2.2.2.3.1. [通过sysTransOrderNo查询订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-pas-sys-query-order)
###### 6.19.2.2.2.3.2. [通过mercOrderNo查询订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-pas-merc-query-order)
###### 6.19.2.2.2.4. [申请退款](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-pas--refund)
###### 6.19.2.2.2.5. [退款结果回调通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-pas-refund-notify)
####### 6.19.2.2.2.6. 查询退款订单

###### 6.19.2.2.2.6.1. [通过sysRefundOrderNo查询退款订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-pas-sys-query-refund)
###### 6.19.2.2.2.6.2. [通过mercRefundOrderNo查询退款订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-pas-merc-query-refund)
###### 6.19.2.2.2.7. [签约结果回调通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-pas-withhold-sign-notify)
####### 6.19.2.2.2.8. 查询签约订单

###### 6.19.2.2.2.8.1. [通过mercContractCode查询签约订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-pas-withhold-query-contractcode)
###### 6.19.2.2.2.8.2. [通过contractId查询签约订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-pas-withhold-query-contractid)
###### 6.19.2.2.2.9. [申请解约](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-pas-withhold-unsign)
###### 6.19.2.2.2.10. [解约结果回调通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-pas-withhold-unsign-notify)
###### 6.19.2.2.3. 签约代扣

###### 6.19.2.2.3.1. [预签约](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-withhold-presign)
###### 6.19.2.2.3.2. [签约结果回调通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-withhold-sign-notify)
###### 6.19.2.2.3.3. [申请免密代扣](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-withhold-apply)
###### 6.19.2.2.3.4. [代扣结果回调通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-withhold-notify)
####### 6.19.2.2.3.5. 查询签约订单

###### 6.19.2.2.3.5.1. [通过mercContractCode查询签约订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-withhold-query-contractcode)
###### 6.19.2.2.3.5.2. [通过contractId查询签约订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-withhold-query-contractid)
####### 6.19.2.2.3.6. 查询代扣订单

###### 6.19.2.2.3.6.1. [通过sysTransOrderNo查询订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-withhold-query-sys-order)
###### 6.19.2.2.3.6.2. [通过mercOrderNo查询订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-withhold-query-merc-order)
###### 6.19.2.2.3.7. [申请解约](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-withhold-unsign)
###### 6.19.2.2.3.8. [解约结果回调通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-withhold-unsign-notify)
###### 6.19.2.2.3.9. [申请退款](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-withhold-refunds)
###### 6.19.2.2.3.10. [退款结果回调通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-withhold-refunds-notify)
####### 6.19.2.2.3.11. 查询退款订单

###### 6.19.2.2.3.11.1. [通过sysRefundOrderNo查询退款订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-withhold-query-sys-refund-order)
###### 6.19.2.2.3.11.2. [通过mercRefundOrderNo查询退款订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-withhold-query-merc-refund-order)
###### 6.19.2.2.4. 账单

###### 6.19.2.2.4.1. [查询对账单](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-query-trade-bill)
###### 6.19.2.2.4.2. [查询结算账单](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-query-settle-bill)
##### 6.19.2.3. 平台类商户/服务商

###### 6.19.2.3.1. 基础支付

###### 6.19.2.3.1.1. [预下单](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-agent-prepay)
###### 6.19.2.3.1.2. [关闭订单](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-orders-close)
###### 6.19.2.3.1.3. [支付结果回调通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-agent-pay-notify)
####### 6.19.2.3.1.4. 查询支付订单

###### 6.19.2.3.1.4.1. [通过sysTransOrderNo查询订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-agent-sys-query-order)
###### 6.19.2.3.1.4.2. [通过mercOrderNo查询订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-agent-merc-query-order)
###### 6.19.2.3.1.5. [申请退款](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-agent-refund)
###### 6.19.2.3.1.6. [退款结果回调通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-agent-refund-notify)
####### 6.19.2.3.1.7. 查询退款订单

###### 6.19.2.3.1.7.1. [通过sysRefundOrderNo查询退款订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-agent-sys-query-refund)
###### 6.19.2.3.1.7.2. [通过mercRefundOrderNo查询退款订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-agent-merc-query-refund)
###### 6.19.2.3.2. 支付并签约

###### 6.19.2.3.2.1. [预下单](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-pas-prepay)
###### 6.19.2.3.2.2. [支付结果回调通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-pas-pay-notify)
####### 6.19.2.3.2.3. 查询支付订单

###### 6.19.2.3.2.3.1. [通过sysTransOrderNo查询订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-pas-sys-query-order)
###### 6.19.2.3.2.3.2. [通过mercOrderNo查询订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-pas-merc-query-order)
###### 6.19.2.3.2.4. [申请退款](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-pas-refund)
###### 6.19.2.3.2.5. [退款结果回调通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-pas-refund-notify)
####### 6.19.2.3.2.6. 查询退款订单

###### 6.19.2.3.2.6.1. [通过sysRefundOrderNo查询退款订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-pas-sys-query-refund)
###### 6.19.2.3.2.6.2. [通过mercRefundOrderNo查询退款订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-pas-merc-query-refund)
###### 6.19.2.3.2.7. [签约结果回调通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-pas-sign-notify)
####### 6.19.2.3.2.8. 查询签约订单

###### 6.19.2.3.2.8.1. [通过mercContractCode查询签约信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-pas-query-contractcode)
###### 6.19.2.3.2.8.2. [通过contractId查询签约信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-pas-query-contractid)
###### 6.19.2.3.2.9. [申请解约](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-pas-unsign)
###### 6.19.2.3.2.10. [解约结果回调通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-pas-unsign-notify)
###### 6.19.2.3.3. 签约代扣

###### 6.19.2.3.3.1. [预签约](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-withhold-presign)
###### 6.19.2.3.3.2. [签约结果回调通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-withhold-sign-notify)
###### 6.19.2.3.3.3. [申请免密代扣](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-withhold-apply)
###### 6.19.2.3.3.4. [代扣结果回调通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-withhold-notify)
####### 6.19.2.3.3.5. 查询签约订单

###### 6.19.2.3.3.5.1. [通过mercContractCode查询签约信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-withhold-query-contractcode)
###### 6.19.2.3.3.5.2. [通过contractId查询签约信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-withhold-query-contractid)
####### 6.19.2.3.3.6. 查询代扣订单

###### 6.19.2.3.3.6.1. [通过sysTransOrderNo查询订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-withhold-query-sys-order)
###### 6.19.2.3.3.6.2. [通过mercOrderNo查询订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-withhold-query-merc-order)
###### 6.19.2.3.3.7. [申请解约](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-withhold-unsign)
###### 6.19.2.3.3.8. [解约结果回调通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-withhold-unsign-notify)
###### 6.19.2.3.3.9. [申请退款](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-withhold-refunds)
###### 6.19.2.3.3.10. [退款结果回调通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-withhold-refunds-notify)
####### 6.19.2.3.3.11. 查询退款订单

###### 6.19.2.3.3.11.1. [通过sysRefundOrderNo查询退款订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-withhold-query-sys-refund-order)
###### 6.19.2.3.3.11.2. [通过mercRefundOrderNo查询退款订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-withhold-query-merc-refund-order)
###### 6.19.2.3.4. 合单支付（仅支持平台类商户）

###### 6.19.2.3.4.1. [预下单](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-combined-app-prepay)
###### 6.19.2.3.4.2. [关闭合单支付订单](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-combined-orders-close)
###### 6.19.2.3.4.3. [合单支付结果回调通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-combined-notify)
####### 6.19.2.3.4.4. 查询合单支付订单

###### 6.19.2.3.4.4.1. [通过combinedSysTransOrderNo查询订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-combined-sys-query-order)
###### 6.19.2.3.4.4.2. [通过combinedMercOrderNo查询订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-combined-merc-query-order)
###### 6.19.2.3.4.5. [申请退款](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-combined-refund)
###### 6.19.2.3.4.6. [退款结果回调通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-combined-refund-notify)
####### 6.19.2.3.4.7. 查询退款订单

###### 6.19.2.3.4.7.1. [通过sysRefundOrderNo查询退款订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-combined-sys-query-refund)
###### 6.19.2.3.4.7.2. [通过mercRefundOrderNo查询退款订单信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-combined-merc-query-refund)
###### 6.19.2.3.5. 账单

###### 6.19.2.3.5.1. [查询对账单](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-agent-query-trade-bill)
###### 6.19.2.3.5.2. [查询结算账单](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-partner-agent-query-settle-bill)
##### 6.19.2.4. 通用接口

###### 6.19.2.4.1. [获取应用级凭证](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-api-common-get-app-token)
###### 6.19.2.4.2. 实名信息验证与授权

###### 6.19.2.4.2.1. [实名信息预验证](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-api-common-verification-preverify)
###### 6.19.2.4.2.2. [实名信息验证结果查询](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-api-common-verification-result)
###### 6.19.2.4.2.3. [实名信息授权结果查询](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-api-common-auth-result)
###### 6.19.2.4.3. 人脸核身实人验证

###### 6.19.2.4.3.1. [人脸核身实人预验证](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-api-common-face-verifactaion-preverify)
###### 6.19.2.4.3.2. [人脸核身实人验证结果查询](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-api-common-face-verifactaion-result)
###### 6.19.2.4.4. 运营工具

####### 6.19.2.4.4.1. 商家券

######## 6.19.2.4.4.1.1. 券批次

###### 6.19.2.4.4.1.1.1. [创建券批次](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-api-common-promotion-service-merc-coup-coupbatch-create)
###### 6.19.2.4.4.1.1.2. [修改券批次信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-api-common-promotion-service-merc-coup-coupbatch-update)
###### 6.19.2.4.4.1.1.3. [查询券批次详情](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-api-common-promotion-service-merc-coup-coupbatch-query)
###### 6.19.2.4.4.1.1.4. [上传券预存Code](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-api-common-promotion-service-merc-coup-coupbatch-upload)
###### 6.19.2.4.4.1.1.5. [修改券批次预算](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-api-common-promotion-service-merc-coup-coupbatch-upbudge)
###### 6.19.2.4.4.1.1.6. [设置回调通知地址](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-api-common-promotion-service-merc-coup-coupbatch-callbackurl-update)
###### 6.19.2.4.4.1.1.7. [查询回调通知地址](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-api-common-promotion-service-merc-coup-coupbatch-callbackurl-select)
######## 6.19.2.4.4.1.2. 用户券

###### 6.19.2.4.4.1.2.1. [发放优惠券](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-api-common-promotion-service-merc-coup-ucoup-distribute)
###### 6.19.2.4.4.1.2.2. [发券事件回调通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-api-common-promotion-service-merc-coup-ucoup-callback-distribute)
###### 6.19.2.4.4.1.2.3. [核销优惠券](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-api-common-promotion-service-merc-coup-ucoup-use)
###### 6.19.2.4.4.1.2.4. [申请退券](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-api-common-promotion-service-merc-coup-ucoup-refund)
###### 6.19.2.4.4.1.2.5. [使券失效](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-api-common-promotion-service-merc-coup-ucoup-deactivate)
###### 6.19.2.4.4.1.2.6. [查询用户优惠券列表](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-api-common-promotion-service-merc-coup-ucoup-query)
###### 6.19.2.4.4.1.2.7. [查询用户单张优惠券详情](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-api-common-promotion-service-merc-coup-ucoup-query-one)
###### 6.19.2.4.4.2. [查询用户可用平台券](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-api-common-promotion-service-inquiry)
##### 6.19.2.5. [REST API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-error-code-rest)
#### 6.19.3. [数据模型说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-model)
#### 6.19.4. [附录](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-appendix)
### 6.20. PDF Kit（PDF服务）

#### 6.20.1. ArkTS API

##### 6.20.1.1. [pdfService（PDF服务）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pdf-arkts-pdfservice)
##### 6.20.1.2. [pdfViewManager（PDF预览）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pdf-arkts-pdfviewmanage)
#### 6.20.2. ArkTS组件

##### 6.20.2.1. [PdfView（PDF预览组件）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pdf-arkts-pdfview-component)
#### 6.20.3. [ArkTS API 错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pdf)
### 6.21. Preview Kit（文件预览服务）

#### 6.21.1. ArkTS API

##### 6.21.1.1. [filePreview（文件预览）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/preview-arkts)
##### 6.21.1.2. [openFileBoost（文件打开加速）（已废弃）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/preview-arkts-openfileboost-api)
##### 6.21.1.3. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preview)
#### 6.21.2. C API

##### 6.21.2.1. 模块

###### 6.21.2.1.1. [Preview](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview)
##### 6.21.2.2. 头文件和结构体

###### 6.21.2.2.1. 头文件

###### 6.21.2.2.1.1. [open_file_boost.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost-open__file__boost_8h)
###### 6.21.2.2.1.2. [file_cache_boost.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost-file__cache__boost_8h)
###### 6.21.2.2.1.3. [preview_kit.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost-preview__kit_8h)
### 6.22. Push Kit（推送服务）

#### 6.22.1. ArkTS API

##### 6.22.1.1. [AAID（应用匿名标识符）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-aaid-api)
##### 6.22.1.2. [pushCommon（推送服务公共信息）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-pushcommon)
##### 6.22.1.3. [pushService（推送服务基础能力）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-pushservice)
##### 6.22.1.4. [RemoteNotificationExtensionAbility（通知扩展Ability）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-remote-notification-extension-ability)
##### 6.22.1.5. [RemoteNotificationExtensionContext（通知扩展Context）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-remote-notification-extension-context)
##### 6.22.1.6. [serviceNotification（服务通知）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-servicenotification)
##### 6.22.1.7. [VoIPExtensionAbility（应用内通话消息扩展Ability）（废弃）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-voip-ability)
##### 6.22.1.8. [VoIPExtensionContext（应用内通话消息扩展Context）（废弃）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-voip-context)
##### 6.22.1.9. [PushExtensionAbility（推送扩展Ability）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-extension-ability)
##### 6.22.1.10. [PushExtensionContext（推送扩展Context）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-extension-context)
##### 6.22.1.11. [RemoteLocationExtensionAbility（定位扩展Ability）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-location-ability)
##### 6.22.1.12. [RemoteLocationExtensionContext（定位扩展Context）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-location-context)
##### 6.22.1.13. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-error-code)
#### 6.22.2. REST API

##### 6.22.2.1. [安全访问要求](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-safety)
##### 6.22.2.2. [图片风控](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-image-control)
##### 6.22.2.3. 场景化消息推送

###### 6.22.2.3.1. [功能介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-scenariozed-api-intro)
###### 6.22.2.3.2. [请求体结构说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-scenariozed-api-request-struct)
###### 6.22.2.3.3. [请求体参数说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-scenariozed-api-request-param)
###### 6.22.2.3.4. [响应参数](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-scenariozed-api-response)
###### 6.22.2.3.5. [请求示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-scenariozed-api-request-example)
###### 6.22.2.3.6. [消息频控](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-msg-freq-control)
##### 6.22.2.4. [消息撤回](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-msg-revoke)
##### 6.22.2.5. [消息回执](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-api-msg-receipt)
##### 6.22.2.6. [服务通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-api-service-noti)
##### 6.22.2.7. 服务动态

###### 6.22.2.7.1. [服务动态推送接口](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-api-service-timeline-send)
###### 6.22.2.7.2. [服务动态参数说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-api-service-timeline-param)
### 6.23. Reader Kit（阅读服务）

#### 6.23.1. ArkTS API

##### 6.23.1.1. [bookParser（书籍解析能力）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/reader-book-parser)
##### 6.23.1.2. [readerCore（阅读核心能力）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/reader-read-core)
#### 6.23.2. ArkTS组件

##### 6.23.2.1. [ReadPageComponent（阅读页组件）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/reader-api-readpagecomponent)
#### 6.23.3. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/reader-error-code)
### 6.24. Scenario Fusion Kit（融合场景服务）

#### 6.24.1. ArkTS API

##### 6.24.1.1. [atomicService（融合场景化API）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scenario-fusion-atomicservice)
##### 6.24.1.2. [fileUriService（文件路径转换API）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scenario-fusion-fileuriresult)
##### 6.24.1.3. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-scenario-fusion-arkts-api)
#### 6.24.2. ArkTS组件

##### 6.24.2.1. [FunctionalButton（Button组件）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scenario-fusion-functionalbutton)
##### 6.24.2.2. [functionalButtonComponentManager(场景化融合Button组件管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scenario-fusion-functionalbuttoncomponentmanager)
##### 6.24.2.3. [FunctionalInput（Input组件）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scenario-fusion-functionalinput)
##### 6.24.2.4. [functionalInputComponentManager(场景化融合Input组件管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scenario-fusion-functionalinputcomponentmanager)
##### 6.24.2.5. [ArkTS组件错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-scenario-fusion)
### 6.25. Screen Time Guard Kit（屏幕时间守护服务）

#### 6.25.1. ArkTS API

##### 6.25.1.1. [@hms.utilityApplication.screenTimeGuard.guardService.d.ts（屏幕时间守护服务）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/screentimeguard-guardservice)
##### 6.25.1.2. [@hms.utilityApplication.screenTimeGuard.appPicker.d.ts（应用选择）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/screentimeguard-app-picker)
##### 6.25.1.3. [@hms.utilityApplication.screenTimeGuard.TimeGuardExtensionAbility.d.ts（屏幕时间守护扩展Ability）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/screentimeguard-timeguardextensionability)
##### 6.25.1.4. [@hms.utilityApplication.screenTimeGuard.TimeGuardExtensionContext.d.ts（屏幕时间守护扩展Context）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/screentimeguard-timeguardextensioncontext)
##### 6.25.1.5. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-screentimeguard)
### 6.26. Share Kit（分享服务）

#### 6.26.1. ArkTS API

##### 6.26.1.1. [systemShare（分享）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/share-system-share)
##### 6.26.1.2. [harmonyShare（华为分享）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/share-harmony-share)
##### 6.26.1.3. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/share-error-code)
### 6.27. Wallet Kit（钱包服务）

#### 6.27.1. ArkTS API

##### 6.27.1.1. [walletPass（Pass卡片能力）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wallet-walletpass)
##### 6.27.1.2. [walletTransitCard（交通卡能力）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wallet-wallettransitcard)
##### 6.27.1.3. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-wallet)
#### 6.27.2. REST API

##### 6.27.2.1. [公共说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wallet-rest-api-introduction)
##### 6.27.2.2. [公共接口](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wallet-rest-api-public)
##### 6.27.2.3. [数字车钥匙接口](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wallet-rest-api-carkey)
##### 6.27.2.4. [REST API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wallet-rest-api-error-code)
### 6.28. Weather Service Kit（天气服务）

#### 6.28.1. ArkTS API

##### 6.28.1.1. [weatherService（天气数据服务）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/weather-service-weatherservice)
##### 6.28.1.2. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/weather-service-error-code)

## 7. AI

### 7.1. Agent Framework Kit（智能体框架服务）

#### 7.1.1. ArkTS组件

##### 7.1.1.1. [FunctionComponent（功能组件）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/hmaf-function-component)
#### 7.1.2. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-agent-framework)
### 7.2. CANN Kit（CANN异构计算框架服务）

#### 7.2.1. C API

##### 7.2.1.1. 模块

###### 7.2.1.1.1. [CANN](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit)
##### 7.2.1.2. 头文件和结构体

###### 7.2.1.2.1. 头文件

###### 7.2.1.2.1.1. [hiai_aipp_param.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit-hiai-aipp-param-8h)
###### 7.2.1.2.1.2. [hiai_helper.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit-hiai-helper-8h)
###### 7.2.1.2.1.3. [hiai_options.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit-hiai-options-8h)
###### 7.2.1.2.1.4. [hiai_single_op.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit-hiai-single-op-8h)
###### 7.2.1.2.1.5. [hiai_tensor.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit-hiai-tensor-8h)
###### 7.2.1.2.1.6. [llm_engine.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit-llm-engine)
###### 7.2.1.2.2. 结构体

###### 7.2.1.2.2.1. [HiAISingleOpDescriptor_ConvolutionParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit-sopdesc-convparam)
###### 7.2.1.2.2.2. [HiAI_SingleOpExecutorConvolutionParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit-sopexec-convparam)
###### 7.2.1.2.2.3. [HiAI_SingleOpExecutorFusedConvolutionActivationParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit-sopexec-fusedconv-actparam)
### 7.3. Core Speech Kit（基础语音服务）

#### 7.3.1. ArkTS API

##### 7.3.1.1. [textToSpeech（文本转语音）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/hms-ai-texttospeech)
##### 7.3.1.2. [speechRecognizer（语音识别）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/hms-ai-speechrecognizer)
#### 7.3.2. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-corespeech)
### 7.4. Core Vision Kit（基础视觉服务）

#### 7.4.1. ArkTS API

##### 7.4.1.1. [textRecognition（文字识别）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-vision-text-recognition-api)
##### 7.4.1.2. [faceDetector（人脸检测）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-vision-face-detector-api)
##### 7.4.1.3. [faceComparator（人脸比对）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-vision-facecomparator-api)
##### 7.4.1.4. [subjectSegmentation（主体分割）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-vision-subjectsegmentation-api)
##### 7.4.1.5. [visionBase（Core Vision Kit基类）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-vision-vision-base-api)
##### 7.4.1.6. [objectDetection（多目标识别）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-vision-object-detection-api)
##### 7.4.1.7. [skeletonDetection（骨骼点检测）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-vision-skeleton-detection-api)
##### 7.4.1.8. [imageSuperResolution（图像超分）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-vision-image-super-resolution-api)
##### 7.4.1.9. [textSearchImage（通过文本搜索图片）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-vision-text-search-image-api)
#### 7.4.2. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-core-vision)
### 7.5. Intents Kit（意图框架服务）

#### 7.5.1. ArkTS API

##### 7.5.1.1. [insightIntent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/intents-arkts-api-insightintent)
##### 7.5.1.2. [InsightIntentUIExtensionAbility (意图调用UI扩展能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/intents-arkts-api-insightintent-uiextension)
##### 7.5.1.3. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/intents-arkts-api-errorcodes-insightintent)
#### 7.5.2. REST API

##### 7.5.2.1. [意图共享](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/intents-rest-api-intent-share)
##### 7.5.2.2. [事件撤销](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/intents-rest-api-revoke-event)
### 7.6. Natural Language Kit（自然语言理解服务）

#### 7.6.1. ArkTS API

##### 7.6.1.1. [textProcessing（文本处理）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/natural-language-text-processing-api)
##### 7.6.1.2. [wordTag（词性）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/natural-language-word-tag-api)
##### 7.6.1.3. [jsonObject（实体的其他字段）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/natural-language-json-object-api)
#### 7.6.2. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-natural-language)
### 7.7. MindSpore Lite Kit（昇思推理框架服务）

#### 7.7.1. ArkTS API

##### 7.7.1.1. [@ohos.ai.mindSporeLite (端侧AI框架)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-mindsporelite)
#### 7.7.2. C API

##### 7.7.2.1. 模块

###### 7.7.2.1.1. [MindSpore](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore)
##### 7.7.2.2. 头文件

###### 7.7.2.2.1. [context.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-context-h)
###### 7.7.2.2.2. [data_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-data-type-h)
###### 7.7.2.2.3. [format.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-format-h)
###### 7.7.2.2.4. [model.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-model-h)
###### 7.7.2.2.5. [status.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-status-h)
###### 7.7.2.2.6. [tensor.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-tensor-h)
###### 7.7.2.2.7. [types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-types-h)
##### 7.7.2.3. 结构体

###### 7.7.2.3.1. [OH_AI_TensorHandleArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore-oh-ai-tensorhandlearray)
###### 7.7.2.3.2. [OH_AI_ShapeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore-oh-ai-shapeinfo)
###### 7.7.2.3.3. [OH_AI_CallBackParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore-oh-ai-callbackparam)
###### 7.7.2.3.4. [NNRTDeviceDesc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore-nnrtdevicedesc)
###### 7.7.2.3.5. [OH_AI_ContextHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore-oh-ai-contexthandle)
###### 7.7.2.3.6. [OH_AI_DeviceInfoHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore-oh-ai-deviceinfohandle)
###### 7.7.2.3.7. [OH_AI_TensorHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore-oh-ai-tensorhandle)
###### 7.7.2.3.8. [OH_AI_AllocatorHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore-oh-ai-allocatorhandle)
###### 7.7.2.3.9. [OH_AI_ModelHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore-oh-ai-modelhandle)
###### 7.7.2.3.10. [OH_AI_TrainCfgHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore-oh-ai-traincfghandle)
### 7.8. Neural Network Runtime Kit（Neural Network运行时服务）

#### 7.8.1. C API

##### 7.8.1.1. 模块

###### 7.8.1.1.1. [NeuralNetworkRuntime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime)
##### 7.8.1.2. 头文件

###### 7.8.1.2.1. [neural_network_core.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-core-h)
###### 7.8.1.2.2. [neural_network_runtime.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-h)
###### 7.8.1.2.3. [neural_network_runtime_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h)
##### 7.8.1.3. 结构体

###### 7.8.1.3.1. [OH_NN_UInt32Array](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-oh-nn-uint32array)
###### 7.8.1.3.2. [OH_NN_QuantParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-oh-nn-quantparam)
###### 7.8.1.3.3. [OH_NN_Tensor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-oh-nn-tensor)
###### 7.8.1.3.4. [OH_NN_Memory](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-oh-nn-memory)
###### 7.8.1.3.5. [OH_NNModel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-oh-nnmodel)
###### 7.8.1.3.6. [OH_NNCompilation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-oh-nncompilation)
###### 7.8.1.3.7. [OH_NNExecutor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-oh-nnexecutor)
###### 7.8.1.3.8. [NN_QuantParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-nn-quantparam)
###### 7.8.1.3.9. [NN_TensorDesc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-nn-tensordesc)
###### 7.8.1.3.10. [NN_Tensor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-nn-tensor)
### 7.9. Speech Kit（场景化语音服务）

#### 7.9.1. ArkTS API

##### 7.9.1.1. [TextReader（朗读控件）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/speech-textreader-api)
##### 7.9.1.2. [ReadStateCode（播报状态）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/speech-readstatecode)
##### 7.9.1.3. [WindowManager（窗口管理）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/speech-windowmanager)
#### 7.9.2. ArkTS组件

##### 7.9.2.1. [TextReaderIcon（朗读听筒图标）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/speech-textreadericon)
##### 7.9.2.2. [TextReaderIconV2（朗读听筒图标）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/speech-textreadericonv2)
##### 7.9.2.3. [AICaptionComponent（AI字幕组件）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/speech-aicaptioncomponent)
#### 7.9.3. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-speech)
### 7.10. Vision Kit（场景化视觉服务）

#### 7.10.1. ArkTS API

##### 7.10.1.1. [interactiveLiveness（人脸活体检测）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-interactive-liveness)
##### 7.10.1.2. [visionImageAnalyzer（AI识图控件）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-image-analyzer)
#### 7.10.2. ArkTS组件

##### 7.10.2.1. [CardRecognition（卡证识别控件）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-card-recognition)
##### 7.10.2.2. [DocumentScanner（文档扫描控件）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-document-scanner)
#### 7.10.3. [ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-vision)

## 8. 公共基础能力

### 8.1. ArkTS API

#### 8.1.1. [Console (控制台)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-logs)
#### 8.1.2. [loadNativeModule (同步动态加载系统库接口)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-common-load-native-module)
#### 8.1.3. [SysCap (系统能力)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-syscap)
#### 8.1.4. [Timer (定时器)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-timer)
### 8.2. C API

#### 8.2.1. 模块

##### 8.2.1.1. [Init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/init)
##### 8.2.1.2. [memory](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-memory)
##### 8.2.1.3. [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)
#### 8.2.2. 头文件

##### 8.2.2.1. [syscap_ndk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/syscap__ndk_8h)
##### 8.2.2.2. [purgeable_memory.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-purgeable-memory-h)
##### 8.2.2.3. [jsvm.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-h)
##### 8.2.2.4. [jsvm_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)
#### 8.2.3. 结构体

##### 8.2.3.1. [JSVM_CallbackStruct](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-callbackstruct)
##### 8.2.3.2. [JSVM_HeapStatistics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-heapstatistics)
##### 8.2.3.3. [JSVM_InitOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-initoptions)
##### 8.2.3.4. [JSVM_CreateVMOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-createvmoptions)
##### 8.2.3.5. [JSVM_VMInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-vminfo)
##### 8.2.3.6. [JSVM_PropertyDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-propertydescriptor)
##### 8.2.3.7. [JSVM_ExtendedErrorInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-extendederrorinfo)
##### 8.2.3.8. [JSVM_TypeTag](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-typetag)
##### 8.2.3.9. [JSVM_PropertyHandlerConfigurationStruct](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-propertyhandlerconfigurationstruct)
##### 8.2.3.10. [JSVM_ScriptOrigin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-scriptorigin)
##### 8.2.3.11. [JSVM_CompileOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-compileoptions)
##### 8.2.3.12. [JSVM_CodeCache](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-codecache)
##### 8.2.3.13. [JSVM_PropertyHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-propertyhandler)
##### 8.2.3.14. [JSVM_DefineClassOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-defineclassoptions)
##### 8.2.3.15. [JSVM_VM__*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-vm--8h)
##### 8.2.3.16. [JSVM_VMScope__*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-vmscope--8h)
##### 8.2.3.17. [JSVM_EnvScope__*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-envscope--8h)
##### 8.2.3.18. [JSVM_Script__*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-script--8h)
##### 8.2.3.19. [JSVM_Env__*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-env--8h)
##### 8.2.3.20. [JSVM_CpuProfiler__*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-cpuprofiler--8h)
##### 8.2.3.21. [JSVM_Value__*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-value--8h)
##### 8.2.3.22. [JSVM_Data__*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-data--8h)
##### 8.2.3.23. [JSVM_Ref__*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-ref--8h)
##### 8.2.3.24. [JSVM_HandleScope__*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-handlescope--8h)
##### 8.2.3.25. [JSVM_EscapableHandleScope__*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-escapablehandlescope--8h)
##### 8.2.3.26. [JSVM_CallbackInfo__*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-callbackinfo--8h)
##### 8.2.3.27. [JSVM_Deferred__*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-deferred--8h)
##### 8.2.3.28. [JSVM_CallbackStruct*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-callbackstruct8h)
##### 8.2.3.29. [JSVM_PropertyHandlerConfigurationStruct*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-propertyhandlerconfigurationstruct8h)
##### 8.2.3.30. [JSVM_CompileProfile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-compileprofile)
##### 8.2.3.31. [PurgMem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-memory-purgmem)
##### 8.2.3.32. [JSVM_DeserializeResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-deserializeresult)

## 9. 标准库

### 9.1. [libc标准库](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/musl)
### 9.2. [c++标准库](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cpp)
### 9.3. [Node-API](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/napi)
### 9.4. [libuv](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/libuv)
### 9.5. [OpenSL ES](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/opensles)
### 9.6. [OpenGL ES](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/opengles)
### 9.7. [OpenGL](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/opengl)
### 9.8. [EGL](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/egl)
### 9.9. [ICU4C](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/icu4c)
### 9.10. [zlib](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/zlib)
### 9.11. Vulkan

#### 9.11.1. Vulkan开发指导

##### 9.11.1.1. [Vulkan开发概述](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vulkan-overview)
##### 9.11.1.2. [Vulkan Surface开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vulkan-guidelines)
##### 9.11.1.3. [Vulkan External Memory开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vulkan-oh-external-memory-guidelines)
#### 9.11.2. [Vulkan支持能力](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vulkan)
#### 9.11.3. Vulkan扩展能力

##### 9.11.3.1. [Vulkan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan)
##### 9.11.3.2. [vulkan_ohos.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-ohos-h)
##### 9.11.3.3. [VkSurfaceCreateInfoOHOS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vksurfacecreateinfoohos)
##### 9.11.3.4. [VkNativeBufferOHOS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vknativebufferohos)
##### 9.11.3.5. [VkSwapchainImageCreateInfoOHOS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vkswapchainimagecreateinfoohos)
##### 9.11.3.6. [VkPhysicalDevicePresentationPropertiesOHOS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vkphysicaldevicepresentationpropertiesohos)
##### 9.11.3.7. [VkNativeBufferUsageOHOS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vknativebufferusageohos)
##### 9.11.3.8. [VkNativeBufferPropertiesOHOS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vknativebufferpropertiesohos)
##### 9.11.3.9. [VkNativeBufferFormatPropertiesOHOS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vknativebufferformatpropertiesohos)
##### 9.11.3.10. [VkImportNativeBufferInfoOHOS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vkimportnativebufferinfoohos)
##### 9.11.3.11. [VkMemoryGetNativeBufferInfoOHOS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vkmemorygetnativebufferinfoohos)
##### 9.11.3.12. [VkExternalFormatOHOS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vkexternalformatohos)
##### 9.11.3.13. [NativeWindow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-nativewindow)
##### 9.11.3.14. [OHBufferHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-ohbufferhandle)
##### 9.11.3.15. [OH_NativeBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-oh-nativebuffer)
### 9.12. [HiTSS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/hitss-api-ref)
### 9.13. 附录

#### 9.13.1. [Native api中没有导出的符号列表](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/musl-peculiar-symbol)
#### 9.13.2. [NDK涉及的musl libc接口使用限制的说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/guidance-on-ndk-libc-interfaces-affected-by-permissions)
#### 9.13.3. [Native api中导出的EGL符号列表](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/egl-symbol)
#### 9.13.4. [Native api中导出的ICU4C符号列表](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/icu4c-symbol)
#### 9.13.5. [Native api中导出的OpenGL ES 3.2符号列表](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openglesv3-symbol)
#### 9.13.6. [OpenGL符号列表](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/opengl-symbol)
#### 9.13.7. [Seccomp开放系统调用列表](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/seccomp-symbol)

def community_registration_brokenlink():
    #Clicks at point (327, 15) of the 'MSTaskListWClass' object.
    Aliases.explorer.wndShell_TrayWnd.ReBarWindow32.MSTaskSwWClass.MSTaskListWClass.Click(327, 15)
    #Clicks the 'BrowserWindow' control.
    Aliases.browser.BrowserWindow.Maximize()
    #Opens the specified URL in a running instance of the specified browser.
    Browsers.Item[btFirefox].Navigate("http://dev-dynamic-usgbc.pantheonsite.io/")
    #Clicks at point (109, 26) of the 'linkCommunityRegistration' object.
    Aliases.browser.pageWelcomeToDynamicUsgbcDynamic.headerMainHeader.navNavbarNavbarDefault.navBlockDrupal8ZymphoniesThemeMa.linkCommunityRegistration.Click(109, 26)
    #Waits until the browser loads the page and is ready to accept user input.
    Aliases.browser.pageCommunityFormDynamicUsgbc.Wait()
    #Moves the mouse pointer over the 'panelJsFormItemFormItemJsFormTyp' control.
    Aliases.browser.pageCommunityFormDynamicUsgbc.formUsgbcCommunityRegistrationFo.panelRow.panelColMd12ColXs12.panelColMd8ColXs12UsgbcContainer.panel.panelUsgbcContainerInnerBox.panelUsgbcFormField.panelJsFormItemFormItemJsFormTyp.HoverMouse(479, 13)
    #Verifies the web page using the WebAccessibility1 Stores item.
    WebTesting.WebAccessibility1.Check()

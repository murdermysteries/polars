import { JupyterFrontEnd, JupyterFrontEndPlugin } from '@jupyterlab/application';
import { IThemeManager } from '@jupyterlab/apputils';

/**
 * A plugin for the Nord Light theme
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'jupyterlab-nord-light-theme:plugin',
  requires: [IThemeManager],
  activate: (app: JupyterFrontEnd, manager: IThemeManager) => {
    const style = 'jupyterlab-nord-light-theme/index.css';

    manager.register({
      name: 'Nord Light',
      isLight: true,
      load: () => manager.loadCSS(style),
      unload: () => Promise.resolve(undefined)
    });
  },
  autoStart: true
};

export default plugin;

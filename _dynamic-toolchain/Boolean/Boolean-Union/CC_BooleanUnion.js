import { html } from "lit";
import { Tool } from "../../../src/components/tool_ui/Tool";

export default class CC_BooleanUnion extends Tool { //copied from Array2D
  render() {
    return this.renderModule(html`<div></div>`);
  }
}
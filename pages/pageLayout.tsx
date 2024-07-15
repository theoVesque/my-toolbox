// components/pageLayout.js
import Sidebar from "../components/sidebar/sidebar";
import { ReactNode } from "react";

export default function PageLayout({ children }: { children: ReactNode }) {
  return (
    <div className="flex flex-col lg:flex-row">
      <Sidebar />
      <main className="content ">{children}</main>
    </div>
  );
}

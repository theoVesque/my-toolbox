// pages/_app.js
import "../app/globals.css";
import { Inter } from "next/font/google";
import { ReactNode } from "react";
import Sidebar from "../components/sidebar/sidebar";

const inter = Inter({ subsets: ["latin"] });

export default function MyApp({ Component, pageProps }) {
  return (
    <div className="layout flex flex-col lg:flex-row min-h-[100vh] h-[100%] lg:px-8 lg:py-8 px-2 py-1 bg-light_gray">
      <main className="content">
        <Component {...pageProps} />
      </main>
    </div>
  );
}

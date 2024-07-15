import "./globals.css";
import { Inter } from "next/font/google";
import Sidebar from "../components/sidebar/sidebar";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "My toolbox",
  description: "All tools you need on 1 website",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <meta charSet="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>{metadata.title}</title>
        <meta name="description" content={metadata.description} />
      </head>
      <body className={inter.className}>
        <div className="layout flex flex-col lg:flex-row min-h-[100vh] h-[100%] lg:px-8 lg:py-8 px-2 py-1 bg-light_gray">
          <Sidebar />
          <main className="content">{children}</main>
        </div>
      </body>
    </html>
  );
}

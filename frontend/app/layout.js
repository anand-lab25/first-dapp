// app/layout.js
export const metadata = {
  title: "My DApp",
  description: "Next.js App Router setup",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        {children}
      </body>
    </html>
  );
}

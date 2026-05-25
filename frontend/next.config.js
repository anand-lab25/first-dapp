/** @type {import('next').NextConfig} */
const nextConfig = {
  turbopack: {
    root: __dirname, // force root to frontend/
  },
};

module.exports = nextConfig;

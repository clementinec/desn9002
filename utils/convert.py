import asyncio
import os
import tempfile

from subprocess import PIPE, Popen
from pyppeteer import launch

import concurrent.futures

async def html_to_pdf(html_file, pdf_file, pyppeteer_args=None):
    """Convert a HTML file to a PDF"""
    browser = await launch(
        handleSIGINT=False,
        handleSIGTERM=False,
        handleSIGHUP=False,
        headless=True,
        args=["--no-sandbox"],
    )

    page = await browser.newPage()
    await page.setViewport(dict(width=994, height=768))
    await page.emulateMedia("screen")

    await page.goto(f"file://{html_file}", {"waitUntil": ["networkidle2"]})

    page_margins = {
        "left": "20px",
        "right": "20px",
        "top": "30px",
        "bottom": "30px",
    }

    dimensions = await page.evaluate(
        """() => {
        return {
            width: document.body.scrollWidth,
            height: document.body.scrollHeight,
            offsetWidth: document.body.offsetWidth,
            offsetHeight: document.body.offsetHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }"""
    )
    width = dimensions["width"]
    height = dimensions["height"]

    await page.pdf(
        {
            "path": pdf_file,
            "format": "A4",
            "printBackground": True,
            "margin": page_margins,
        }
    )

    await browser.close()



if __name__ == "__main__":
    
    html_input_file = "/Users/hongshanguo/OneDrive - The University Of Hong Kong/Courses/DESN9002/Presentation Draft/Notebooks/LLMNotes_L1.slides.html?print-pdf"
    pdf_output_file = "slides.pdf"

    pool = concurrent.futures.ThreadPoolExecutor()
    pool.submit(
        asyncio.run,
        html_to_pdf(
            html_input_file,
            pdf_output_file
        ),
    ).result()
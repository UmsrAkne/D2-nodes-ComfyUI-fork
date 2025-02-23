<img src="../img/title.jpg" style="max-width:100%">



<a href="../en/index.md">English</a> | <a href="../ja/index.md">日本語</a> | <a href="../zh/index.md">繁体中文</a>

- <a href="index.md">Top</a>
- <a href="node.md">Node</a>
- <a href="workflow.md">Workflow</a>



# Node

## :tomato: Sampler Nodes

### D2 KSampler / D2 KSampler(Advanced)

<figure>
<img src="../img/ksampler_2.png">
</figure>

- KSampler that can input prompts as STRING

#### Input

- `cnet_stack`
  - For connecting to `D2 Controlnet Loader`
- `model` / `clip` / `vae` / ..etc
    - Same as standard KSampler
- `negative` / `positive`
    - Prompts in STRING format

#### Output

- `IMAGE`
    - Image output
- `positive` / `negative`
    - Input passthrough


---

### D2 Pipe

<figure>
<img src="../img/pipe.png">
</figure>

- A node for modifying and extracting the contents of `d2_pipe`
- `d2_pipe` is used to pass parameters collectively in nodes such as D2 XY Plot Easy, D2 KSampler, and D2 Send Eagle


---

## :tomato: Loader Node

### D2 Checkpoint Loader

<img src="../img/checkpoint_loader_2.png">

- A Checkpoint Loader that outputs the full path of model files
- Can automatically apply v_prediction settings when the filename contains "vpred"

#### Input

- `ckpt_name`
  - Checkpoint name
- `auto_vpred`
  - `true`: Automatically applies v_prediction settings if the filename contains "vpred"
- `sampling` / `zsnr`
  - Same settings as ModelSamplingDiscrete (details unknown)
- `multiplier`
  - Same settings as RescaleCFG (details unknown)

#### Output

- `model` / `clip` / `vae`
    - Same as the conventional CheckpointLoader.
- `ckpt_name` / `ckpt_hash` / `ckpt_fullpath`
    - Checkpoint name, hash, and full path.

---

### D2 Controlnet Loader

<figure>
<img src="../img/controlnet.png">
</figure>

- Controlnet Loader that creates simple workflows when connected to `D2 KSampler`

#### Input

- `cnet_stack`
  - For connecting to `D2 Controlnet Loader`

#### Output

- `cnet_stack`
  - For connecting to `D2 KSampler` or `D2 Controlnet Loader`

---

## :tomato: Image Node


### D2 Preview Image

<figure>
<img src="../img/preview_image_1.png">
<img src="../img/preview_image_2.png">
</figure>

- Click the `Popup Image` button to display the full-screen gallery

---

### D2 Load Image

<figure>
<img src="../img/load_image.png">
</figure>

- Load Image node that can extract prompts from images
- Compatible with images created in StableDiffusion webui A1111 and NovelAI
- Includes a button to open mask editor

#### Input

- `image_path`
  - Loads file when image path is input
  - Used for connection with `D2 Folder Image Queue`

#### Output

- `IMAGE / MASK`
    - Image and mask
- `width / height`
    - Image size
- `positive` / `negative`
    - Prompts

Note: Prompts may not be retrievable depending on workflow configuration. For example, they cannot be retrieved without a node containing the string "KSampler" (e.g., Tiled KSampler).

---

### D2 Load Folder Images

<figure>
<img src="../img/load_folder_images.png">
</figure>

- Batch loads and outputs images from a folder
- Used with `D2 Grid Image` etc.
- Use `D2 Folder Image Queue` for sequential processing

#### Input

- `folder`
  - Specify folder in full path
- `extension`
  - Specify like `*.jpg` to load only JPEG images
  - Can also specify patterns like `*silver*.webp`

---

### D2 Folder Image Queue

<figure>
<img src="../img/folder_image_queue_2.png">
</figure>

- Outputs paths of images in a folder
- Automatically executes Queue for the number of images when Queue is run

#### Input

- `folder`
  - Image folder
- `extension`
  - Specify file name filter
  - `*.*`: All images
  - `*.png`: PNG format only
- `start_at`
  - Image number to start processing
- `auto_queue`
  - `true`: Automatically execute remaining Queues
  - `false`: Execute only once

#### Output

- `image_path`
  - Full path of image

---

### D2 Grid Image

<figure>
<img src="../img/grid_image.png">
</figure>

- Outputs grid images
- Supports both horizontal and vertical alignment

#### Input

- `max_columns`
  - Number of images to align horizontally
  - When `swap_dimensions` is `true`, this becomes the number of vertical images
- `grid_gap`
  - Spacing between images
- `swap_dimensions`
  - `true`: Vertical alignment
  - `false`: Horizontal alignment
- `trigger_count`
  - Outputs grid image when the number of input images reaches this specified value
- `Image count`
  - Number of input images
- `Reset Images`
  - Discards all input images

---

### D2 Image Stack

<figure>
<img src="../img/image_stack.png">
</figure>

- Outputs multiple input images together
- Can input up to 50 images

#### Input

- `image_count`
  - Can increase/decrease number of inputs. Maximum 50

---

### D2 EmptyImage Alpha

<figure>
<img src="../img/empty_image_alpha.png">
</figure>

- Adds alpha channel (transparency) to EmptyImage

---

## :tomato: Size Node

### D2 Get Image Size

<figure>
<img src="../img/get_image_size.png">
</figure>

- Both outputs and displays size

---

### D2 Size Selector

<figure>
<img src="../img/sizeselector_2.png">
</figure>

- Node for selecting image size from presets
- Can also get size from images
- Rounding method can be selected from `Ceil / Float / None`

#### Input

- `images`
    - Used when getting size from images
    - `preset` must be set to `custom`
- `preset`
    - Size presets
    - Must be set to `custom` when using `width` `height` below or image sizes
    - Edit `/custom_nodes/D2-nodes-ComfyUI/config/sizeselector_config.yaml` to modify presets
- `width` / `height`
    - Width/height dimensions
    - `preset` must be set to `custom`
- `swap_dimensions`
    - Swap width/height
- `upscale_factor`
    - Value passed to other resize nodes. Does nothing in this node
- `prescale_factor`
    - Output width/height after resizing by this factor
- `round_method`
    - `Round`: Round to nearest
    - `Floor`: Round down
    - `None`: No rounding
- `batch_size`
    - Batch size to set for empty_latent

#### Output

- `width / height`
    - Input `width`, `height` multiplied by `prescale_factor`
- `upscale_factor` / `prescale_factor`
    - Passthrough of input
- `batch_size`
    - Passthrough of input
- `empty_latent`
    - Outputs latent created with specified size and batch size

---

### D2 Image Resize

<figure>
<img src="../img/image_resize.png">
</figure>

- Simple image resizing
- Precision up to 3 decimal places
- Can select rounding, floor, or ceiling
- Capable of upscaling using upscale models
- Latent output is also possible (requires VAE)

---

### D2 Resize Calculator

<figure>
<img src="../img/resize_calc.png">
</figure>

- Can select rounding, floor, or ceiling

---

## :tomato: Text Node

### D2 Regex Replace

<figure>
<img src="../img/regex_replace_2.png">
</figure>

- Can replace using regular expressions
- Multiple conditions can be specified
- Supports reuse of regex match strings (e.g., \1, \2)
- Target string can be specified by "tag unit" or "whole"

#### Input

- `text`
    - Target string for search
- `mode`
  - `Tag`: Break down `text` by newlines and "," and replace individually
  - `Advanced`: Replace `text` as a whole
- `regex_and_output`
    - List of search strings and output strings
    - Write in following format
    - If output string is empty, matched part is deleted
    - No limit on number of entries

```
Search string 1
--
Output string 1
--
Search string 2
--
Output string 2
```

#### Output

- `text`
    - Text after replacement

#### Sample

Sample for removing Pony series quality tags.

Mode: `Tag`

Input text
```
score_9, score_8_up, (score_7_up, score_6_up:0.8) , rating_explicit, source_anime, BREAK
1girl, swimsuit
```
Regex Replace
```
.*(score_|rating_|source_).*
--
--
BREAK
--

```

Output text
```
1girl, swimsuit
```

---

### D2 Regex Switcher

<img src="../img/regex_switcher_1.png">

- Searches input text with regex and outputs matching text
- Main purpose is switching quality tags per Checkpoint
- When matching string is found in input `text`, outputs target string and match index (starting from 0)
- Can concatenate strings at front and back

#### Input

- `text`
    - Search target string
- `prefix`
    - String to concatenate at front
- `suffix`
    - String to concatenate at back
- `regex_and_output`
    - List of search strings and output strings
    - Write in following format
- `pre_delim`
    - Character inserted between `prefix` and `regex_and_output`
    - `Comma`: `,` / `Line break`: newline / `None`: nothing
- `suf_delim`
    - Character inserted between `regex_and_output` and `suffix`

#### Output

- `combined_text`
    - String combining `prefix` + output string + `suffix`
- `prefix` / `suffix`
    - Input passthrough

---

### D2 Multi Output

<figure>
<img src="../img/multi.png">
</figure>

- Node that outputs generic parameters like seed and cfg as lists

#### Input

- `type`
    - `FLOAT`: Floating point numbers. For CFG etc.
    - `INT`: Integers. For steps etc.
    - `STRING`: Strings. For sampler etc.
    - `SEED`: Can input seed values with random number button
- `Add Random`
    - Adds random numbers to input field
    - Only shown when `type` is `SEED`

---

### D2 Filename Template

<figure>
  <img src="../img/filename_template.png">
</figure>

- A node for creating filenames
- Can incorporate external elements

#### Input

- `arg_1` `arg_2` `arg_3`
  - Import values from other nodes
- `format`
    - `%date:{yyyy/MM/dd/hh/mm/ss}%`
      - `yyyy`: Year
      - `MM`: Month
      - `dd`: Day
      - `hh`: Hour
      - `mm`: Minute
      - `ss`: Second
    - `%node:{id}.{key}%`
      - Retrieves values by specifying node ID and item name
      - Example: `%node:8.width%`: Get width from node ID 8
    - `%arg_1%` (same for 2 and 3)
      - Embed input values
    - `%arg_1:ckpt_name%` (same for 2 and 3)
      - Embed checkpoint name with `.safetensors` removed

#### Example
```
%date:yyyyMMdd-hhmmss%_%arg_1:ckpt_name%
👇
20241219-021926_obsessionIllustrious_v31
```

---


## :tomato: XY Plot Node


### D2 XY Plot Easy

<figure>
<img src="../img/xyplot_easy.png">
</figure>

- A node that creates XY Plots with simplified workflow limited to KSampler parameters

#### Input

- `positive` / `negative` / `seed` / `steps` / `cfg` / `sampler_name` / `scheduler` / `denoise`
  - Settings to pass to KSampler
- `ckpt_name`
  - Setting to pass to D2 Checkpoint Loader
- `x_type` / `y_type`
  - Specify items to execute in XY Plot
  - When `STRING`, `INT`, or `FLOAT` is specified, output will be from `x_other`, `y_other`
- `x_list` / `y_list`
  - XY Plot modification contents
  - Since it's newline-separated text, input from other nodes is possible
- `auto_queue`
  - `true`: Automatically executes Queue the required number of times
  - `false`: Manually execute Queue
- `Reset index`
  - Reset index with this button when stopped midway

#### Output

- `xy_pipe`
  - Collectively outputs parameters used in D2 KSampler
- `grid_pipe`
  - Collectively outputs parameters `x_annotation` `y_annotation` `status` used in D2 Grid Image
- `positive` / `negative` / `seed` / `steps` / `cfg` / `sampler_name` / `scheduler` / `denoise`
  - Parameters to pass to KSampler
- `ckpt_name`
  - Setting to pass to D2 Checkpoint Loader
- `x_other` / `y_other`
  - Outputs from here when `x_type` `y_type` is set to `STRING` `INT` `FLOAT`
- `x_annotation` / `y_annotation`
  - Header text to connect to `D2 XY Grid Image`
- `status`
  - Control signal to connect to `D2 XY Grid Image`
- `index`
  - Current processing count

---


### D2 XY Plot

<figure>
<img src="../img/xyplot.png">
</figure>

- Node for creating versatile XY Plot workflows
- X/Y inputs are simple newline-separated text for easy combination with other nodes

#### Input

- `x_type` / `y_type`
  - Specify data type of `x_list` `y_list` from `STRING` `INT` `FLOAT`
- `x_title` / `y_title`
  - Text to add to header text
- `x_list` / `y_list`
  - XY Plot change contents
  - Newline-separated text that can be input using other nodes
- `auto_queue`
  - `true`: Automatically execute required number of Queues
  - `false`: Manually execute Queue
- `Reset index`
  - Reset index with this button when stopped midway

#### Output

- `X` / `Y`
  - Elements retrieved from `x_list` `y_list`
- `x_annotation` / `y_annotation`
  - Header text to connect to `D2 XY Grid Image`
- `status`
  - Control signal to connect to `D2 XY Grid Image`
- `index`
  - Current processing count

---

### D2 XY Grid Image

<figure>
<img src="../img/xyplot.png">
</figure>

- Grid image creation node used with `D2 XY Plot`

#### Input

- `x_annotation` / `y_annotation`
  - Header text for grid image
- `status`
  - Control text from `D2 XY Plot`
  - `INIT`: Initialize
  - `FINISH`: Output grid image
  - `{empty string}`: Other states
- `font_size`
  - Header text font size
- `grid_gap`
  - Gap between images
- `swap_dimensions`
  - `true`: Vertical grid
  - `false`: Horizontal grid
- `grid_only`
  - `true`: Output only grid image
  - `false`: Output individual images too

---

### D2 XY Prompt SR

<figure>
<img src="../img/prompt_sr_2.png">
</figure>

- Search and replace input text to pass to `D2 XY Plot`
- Can output as list

#### Input

- `prompt`
    - Prompt. Can include newlines
- `search_txt`
    - Search target text. Can include multiple words
    - Cannot use newlines
- `replace`
    - Replacement text
    - OK to include "," as it's separated by newlines

#### Output

- `x / y_list`
  - Connect to `D2 XY Plot`
- `LIST`
  - Output replaced text as list

---

### D2 XY Prompt SR2

<figure>
<img src="../img/prompt_sr2.png?3">
</figure>

- Search and replace prompts received from `D2 XY Plot` before passing to KSampler
- Use this to recreate Stable Diffusion webui A1111's Prompt S/R

#### Input

- `x_y`
  - Replacement text received from `D2 XY Plot`
- `prompt`
    - Target text for replacement
- `search`
    - Search text. Can include multiple words
    - Cannot use newlines

---

### D2 XY Seed

<figure>
<img src="../img/xy_seed.png?2">
</figure>

- Outputs random number when `-1` is specified
- Other numbers are output as-is
- Must set `x/y_type` to `INT` on `D2 XY Plot` side


---


### D2 XY Seed2

<figure>
  <img src="../img/xy_seed2.png?2">
</figure>

- A node that outputs a specified number of seed values

#### input
- `initial_number`
  - This value is used as a reference when `mode` is set to `increment`, `decrement`, or `fixed`
- `count`
  - Number of seed values to generate
- `mode`
  - `fixed`: Outputs only the `initial_number`
  - `increment`: Adds 1 to `initial_number` for each value
  - `decrement`: Subtracts 1 from `initial_number` for each value
  - `randomize`: Outputs random numbers regardless of `initial_number`

---

### D2 XY Checkpoint List / D2 XY Lora List

<figure>
<img src="../img/xy_checkpoint_list.png">
</figure>

- Node to pass Checkpoint/Lora to `D2 XY Plot`
- Can specify up to 50

---

### D2 XY Model List

<figure>
  <img src="../img/xy_model_list.png?2">
</figure>

- A node that passes Checkpoint/Lora to `D2 XY Plot`
- Useful when you want to get a large list of models but don't want to select them one by one in `D2 Checkpoint List`
- Click `get_list` to retrieve the model list, then edit it to keep only the ones you need

#### input
- `model_type`
  - Select either `checkpoints` or `loras`
- `filter`
  - Enter text to filter
  - Regular expressions are supported
  - When including `\` in search text, write it as `\\`
- `get_list`
  - Button to retrieve model list


---


### D2 XY Folder Images

<figure>
<img src="../img/xy_folder_images.png">
</figure>

- Node to pass image paths from specified folder to `D2 XY Plot`

---

### D2 XY Annotation

<figure>
<img src="../img/xy_annotation.png?2">
</figure>

- Used to add headers when not using `D2 XY Plot` or when doing special XY Plot

---

### D2 XY List To Plot

<figure>
  <img src="../img/xy_list_to_plot.png?2">
</figure>

- Converts output from list nodes to be compatible with `D2 XY Plot`
- Internally, it simply performs `"\n".join(list)`, so if the list contents include line breaks, it may not work as intended
- Use `D2 XY String To Plot` when working with text that contains line breaks

---

### D2 XY String To Plot

<figure>
  <img src="../img/xy_string_to_plot.png">
</figure>

- Converts multiline text to be compatible with `D2 XY Plot` / `D2 XY Plot Easy`
- Used when you want to perform XY Plot comparisons of entire prompts
- When using with `D2 XY Plot Easy` for prompt comparison, set `x/y_type` to `STRING` and connect `x/y_other` to the `positive` input of `D2 KSampler`

---


## :tomato: Refiner Node

### D2 Refiner Steps

<figure>
<img src="../img/refiner_steps.png">
</figure>

- Node for outputting steps for Refiner

#### Input

- `steps`
    - Total step count
- `start`
    - Starting steps for first KSampler
- `end`
    - Ending steps for first KSampler

#### Output

- `steps` / `start` / `end`
    - Input passthrough
- `refiner_start`
    - Starting steps for second KSampler

---

### D2 Refiner Steps A1111

<figure>
<img src="../img/refiner_a1111.png">
</figure>

- Node that can specify denoise for Refiner in img2img

#### Input

- `steps`
    - Total step count
- `denoise`
    - Specify denoise for img2img
- `switch_at`
    - What percentage of total steps to switch to next KSampler

#### Output

- `steps`
    - Input passthrough
- `start`
    - Starting steps for first KSampler
- `end`
    - Ending steps for first KSampler
- `refiner_start`
    - Starting steps for second KSampler

---

### D2 Refiner Steps Tester

- Node for checking steps


---


## :tomato: Merge Node


### D2 Model and CLIP Merge SDXL

<figure>
  <img src="../img/merge_sdxl.png">
</figure>

- A node that combines ModelMergeSDXL and CLIPMergeSimple
- Allows comma-separated weight specifications for easier use with XYPlot
- In this figure, `0.85,0.85,1,1,0.4,0.4,1,0.4,0.4,0.4,1,0.4,0.4,0.4,0,0.55,0.85,0.85,0.85,0.85,0.85,0.85,1,1,0.65` is specified



---

## :tomato: Float Palet

### D2 Queue Button

<figure>
<img src="../img/queue_button.png">
</figure>

- Button to generate specified number of images (Batch count)
- Can be moved by dragging left edge of palette

<figure>
<img src="../img/queue_button_setting.png">
</figure>

- Configure visibility in ComfyUI settings under `D2` category
- Number of images can also be set from settings screen
- Separate numbers with comma (,)

---

### Prompt convert dialog

<figure>
<img src="../img/prompt_convert_dialog.png">
</figure>

- Dialog for converting weights between NovelAI and StableDiffusion
- Open from `Prompt convert` button
- Hidden by default
- Enable display by activating `settings > D2 > Show prompt convert button`


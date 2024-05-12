<?php

namespace App\Http\Controllers;

use App\Models\User;
use Illuminate\Http\Request;

class UserController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        $data = User::all();
        return response()->json(['data' => $data], 200);
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        try {
            $request->validate([
                'name' => 'required',
                'email' => 'required'
            ]);
            User::create([
                'name' => $request->name,
                'email' => $request->email
            ]);
            return response()->json(['message' => 'success'], 200);
        } catch (\Throwable $th) {
            return response()->json(['message' => $th], 200);
        }
    }

    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        $data = User::find($id);
        return response()->json(['data' => $data], 200);
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(string $id)
    {
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, string $id)
    {
        try {
            $request->validate([
                'name' => 'required',
                'email' => 'required'
            ]);
            $data = User::find($id);
            $update = $data->update([
                'name' => $request->name,
                'email' => $request->email
            ]);
            if (!$update) {
                return response()->json(['failed', 'failed']);
            }
            return response()->json(['message' => 'success'], 200);
        } catch (\Throwable $th) {
            return response()->json(['message' => $th]);
        }
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        try {
            $data = User::find($id);
            $data->delete();
            if (!$data) {
                return response()->json(['failed'], 400);
            }
            return response()->json(['message' => 'failed'], 200);
        } catch (\Throwable $th) {
            return response()->json(['message' => $th], 400);
        }
    }
}
